from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from datetime import datetime
from pathlib import Path
from typing import List
import re, time
from openpyxl import Workbook
from playwright.sync_api import sync_playwright

# --- Configurações ---
app = FastAPI(title="TV Asa Branca Scraper API (Playwright)", version="2.0.0")
EXCEL_DIR = Path("/data")
EXCEL_DIR.mkdir(exist_ok=True)

URL = "https://redeglobo.globo.com/pe/tvasabranca/programacao/"

# --- Funções ---
def coletar_programacao() -> List[List[str]]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(URL, wait_until="networkidle", timeout=60000)

        # Expandir blocos do acordeão
        try:
            buttons = page.locator(".accordion .accordionTitle button")
            for i in range(buttons.count()):
                try:
                    buttons.nth(i).scroll_into_view_if_needed()
                    buttons.nth(i).click(timeout=2000)
                    time.sleep(0.05)
                except Exception:
                    pass
            time.sleep(0.5)
        except Exception:
            pass

        programacao = []
        dias = page.locator(".accordion")
        for i in range(dias.count()):
            d = dias.nth(i)
            data_id = (d.get_attribute("id") or "")
            data_id = re.sub(r"[^0-9]", "", data_id)
            if len(data_id) < 6:
                continue
            ano, mes = data_id[:4], data_id[4:6]
            dia = (data_id[6:8] or "01")
            data_fmt = f"{dia}/{mes}/{ano}"

            blocos = d.locator(".accordionTitle")
            for j in range(blocos.count()):
                b = blocos.nth(j)
                try:
                    h = b.locator(".accordionTitle__time time p").inner_text().strip()
                except Exception:
                    h = ""
                try:
                    pgr = b.locator(".accordionTitle__name p").inner_text().strip()
                except Exception:
                    pgr = ""
                if h or pgr:
                    programacao.append([data_fmt, h, pgr])

        context.close()
        browser.close()
        return programacao

def salvar_em_excel(programacao, nome):
    wb = Workbook()
    ws = wb.active
    ws.title = "Programação TV Asa Branca"
    ws.append(["Data", "Horário", "Programa"])
    for row in programacao:
        ws.append(row)
    dest = EXCEL_DIR / nome
    wb.save(dest)
    return str(dest)

# --- Endpoints ---
@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.utcnow().isoformat()}

@app.get("/")
def root():
    return {"ok": True, "excel_endpoint": "/programacao/semana.xlsx"}

@app.get("/programacao/json")
def programacao_json():
    try:
        prog = coletar_programacao()
        return JSONResponse(content={"count": len(prog), "items": prog})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/programacao/semana.xlsx")
def semana_excel():
    try:
        prog = coletar_programacao()
        nome = f"programacao_tv_asa_branca_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
        path = salvar_em_excel(prog, nome)
        return FileResponse(
            path,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=Path(path).name
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})