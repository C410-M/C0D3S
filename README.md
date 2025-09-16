<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Growth Hacker Directory</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-green: #1E9E16;
            --dark-bg: #333333;
            --black: #000000;
            --white: #FFFFFF;
            --light-gray: #2a2a2a;
            --border-gray: #404040;
            --text-secondary: #b0b0b0;
        }

        body {
            background: linear-gradient(135deg, #000000 0%, #1a1a1a 50%, #000000 100%);
            color: var(--white);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 60px;
            padding: 40px 0;
            background: linear-gradient(135deg, var(--primary-green), #28a745);
            border-radius: 16px;
            color: var(--white);
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: repeating-linear-gradient(
                45deg,
                transparent,
                transparent 10px,
                rgba(255,255,255,0.02) 10px,
                rgba(255,255,255,0.02) 20px
            );
            animation: float 20s linear infinite;
        }

        .header::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 20%, rgba(255,255,255,0.1) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(255,255,255,0.05) 0%, transparent 50%);
        }

        .title {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 16px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: relative;
            z-index: 2;
        }

        .subtitle {
            font-size: 1.25rem;
            font-weight: 300;
            margin-bottom: 16px;
            opacity: 0.9;
            position: relative;
            z-index: 2;
        }

        .description {
            font-size: 1.1rem;
            max-width: 700px;
            margin: 0 auto;
            opacity: 0.95;
            position: relative;
            z-index: 2;
        }

        .stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin: 50px 0;
            flex-wrap: wrap;
        }

        .stat-item {
            text-align: center;
            padding: 30px 25px;
            background: var(--dark-bg);
            border: 2px solid var(--border-gray);
            border-radius: 12px;
            transition: all 0.3s ease;
            min-width: 180px;
        }

        .stat-item:hover {
            border-color: var(--primary-green);
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(30, 158, 22, 0.15);
        }

        .stat-number {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2.5rem;
            color: var(--primary-green);
            font-weight: 600;
            display: block;
        }

        .stat-label {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-top: 8px;
            font-weight: 500;
        }

        .available-section {
            background: var(--light-gray);
            border-radius: 16px;
            padding: 40px;
            margin: 50px 0;
            border-left: 4px solid var(--primary-green);
        }

        .section-title {
            font-size: 2rem;
            color: var(--white);
            margin-bottom: 20px;
            font-weight: 600;
        }

        .section-description {
            color: var(--text-secondary);
            margin-bottom: 30px;
            font-size: 1.05rem;
        }

        .scripts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }

        .script-card {
            background: var(--dark-bg);
            border: 1px solid var(--border-gray);
            border-radius: 12px;
            padding: 30px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .script-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--primary-green);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.3s ease;
        }

        .script-card:hover::before {
            transform: scaleX(1);
        }

        .script-card:hover {
            border-color: var(--primary-green);
            box-shadow: 0 8px 25px rgba(30, 158, 22, 0.1);
            transform: translateY(-3px);
        }

        .script-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
            display: block;
        }

        .script-title {
            font-size: 1.4rem;
            color: var(--white);
            margin-bottom: 12px;
            font-weight: 600;
        }

        .script-description {
            color: var(--text-secondary);
            margin-bottom: 20px;
            font-size: 0.95rem;
        }

        .script-features {
            list-style: none;
            margin-bottom: 25px;
        }

        .script-features li {
            padding: 6px 0;
            color: var(--text-secondary);
            font-size: 0.9rem;
            position: relative;
            padding-left: 20px;
        }

        .script-features li::before {
            content: '✓';
            color: var(--primary-green);
            font-weight: bold;
            position: absolute;
            left: 0;
        }

        .script-tech {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .tech-tag {
            background: var(--primary-green);
            color: var(--white);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
            font-family: 'JetBrains Mono', monospace;
        }

        .coming-soon {
            background: var(--light-gray);
            color: var(--white);
            border-radius: 16px;
            padding: 40px;
            margin: 50px 0;
            text-align: center;
            border: 1px solid var(--border-gray);
        }

        .coming-soon h3 {
            font-size: 2rem;
            margin-bottom: 16px;
            color: var(--primary-green);
        }

        .coming-soon-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .coming-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .coming-item h4 {
            color: var(--primary-green);
            margin-bottom: 8px;
            font-size: 1.1rem;
        }

        .coming-item p {
            font-size: 0.9rem;
            opacity: 0.8;
        }

        .cta-section {
            background: linear-gradient(135deg, var(--dark-bg), #2c2c2c);
            color: var(--white);
            border-radius: 16px;
            padding: 50px 40px;
            text-align: center;
            margin: 50px 0;
        }

        .cta-title {
            font-size: 2.5rem;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .cta-button {
            background: var(--primary-green);
            color: var(--white);
            padding: 16px 32px;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            margin: 15px 10px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .cta-button:hover {
            background: #169e11;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(30, 158, 22, 0.3);
        }

        .footer {
            text-align: center;
            margin-top: 60px;
            padding: 30px 0;
            border-top: 1px solid var(--border-gray);
            color: var(--text-secondary);
        }

        /* Responsivo */
        @media (max-width: 768px) {
            .title {
                font-size: 2.5rem;
            }
            
            .scripts-grid {
                grid-template-columns: 1fr;
            }
            
            .stats {
                gap: 20px;
            }
            
            .container {
                padding: 20px 15px;
            }
            
            .header {
                padding: 30px 20px;
            }
            
            .available-section,
            .coming-soon,
            .cta-section {
                padding: 30px 20px;
            }
        }

        /* Animações */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes float {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .script-card {
            animation: fadeInUp 0.6s ease-out;
        }

        .script-card:nth-child(2) {
            animation-delay: 0.1s;
        }

        .script-card:nth-child(3) {
            animation-delay: 0.2s;
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1 class="title">Growth Hacker Directory</h1>
            <p class="subtitle">Scripts & Automações para Marketing</p>
            <p class="description">
                Seu arsenal completo de scripts e automações para dominar o marketing digital. 
                Códigos testados, documentados e prontos para implementar em suas estratégias.
            </p>
        </header>

        <div class="stats">
            <div class="stat-item">
                <span class="stat-number">3</span>
                <div class="stat-label">Scripts Disponíveis</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">1</span>
                <div class="stat-label">Categoria Ativa</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">100%</span>
                <div class="stat-label">Open Source</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">∞</span>
                <div class="stat-label">Possibilidades</div>
            </div>
        </div>

        <div class="available-section">
            <h2 class="section-title">📊 Scripts Disponíveis</h2>
            <p class="section-description">
                Automações prontas para capturar e processar dados de marketing com precisão profissional.
            </p>

            <div class="scripts-grid">
                <div class="script-card">
                    <span class="script-icon">🎯</span>
                    <h3 class="script-title">Facebook Lead Ads → Google Sheets</h3>
                    <p class="script-description">
                        Automatiza a coleta de leads do Facebook Lead Ads e os sincroniza em uma planilha do Google Sheets.
                    </p>
                    <ul class="script-features">
                        <li>Processa múltiplos formulários simultaneamente</li>
                        <li>Remove duplicatas baseadas no WhatsApp</li>
                        <li>Captura data/hora real de preenchimento</li>
                        <li>Busca automaticamente o nome dos formulários</li>
                        <li>Log detalhado para debugging</li>
                    </ul>
                    <div class="script-tech">
                        <span class="tech-tag">Google Apps Script</span>
                        <span class="tech-tag">Facebook Graph API</span>
                        <span class="tech-tag">Google Sheets API</span>
                    </div>
                </div>

                <div class="script-card">
                    <span class="script-icon">📈</span>
                    <h3 class="script-title">Facebook Ads Metrics → Histórico Completo</h3>
                    <p class="script-description">
                        Coleta métricas detalhadas de campanhas do Facebook Ads e leads de formulários para análise completa de ROI.
                    </p>
                    <ul class="script-features">
                        <li>Métricas de anúncios por período configurável</li>
                        <li>Combina dados de anúncios + leads</li>
                        <li>Deduplicação inteligente de leads</li>
                        <li>Processamento por datas com rate limiting</li>
                        <li>Logs detalhados e notificação de erros</li>
                    </ul>
                    <div class="script-tech">
                        <span class="tech-tag">Google Apps Script</span>
                        <span class="tech-tag">Facebook Marketing API</span>
                        <span class="tech-tag">Analytics</span>
                    </div>
                </div>

                <div class="script-card">
                    <span class="script-icon">⚡</span>
                    <h3 class="script-title">Facebook Ads Metrics → Atualização Diária</h3>
                    <p class="script-description">
                        Versão otimizada para atualizações diárias das métricas, focando apenas nos dados de hoje com substituição automática.
                    </p>
                    <ul class="script-features">
                        <li>Coleta métricas apenas do dia atual</li>
                        <li>Substitui dados existentes automaticamente</li>
                        <li>Otimizado para execução rápida</li>
                        <li>Ideal para triggers automáticos</li>
                        <li>Processamento limitado para velocidade</li>
                    </ul>
                    <div class="script-tech">
                        <span class="tech-tag">Google Apps Script</span>
                        <span class="tech-tag">Facebook Marketing API</span>
                        <span class="tech-tag">Automation</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="coming-soon">
            <h3>🚀 Próximos Lançamentos</h3>
            <p>Estamos trabalhando em novas automações para ampliar seu arsenal de growth hacking:</p>
            
            <div class="coming-soon-grid">
                <div class="coming-item">
                    <h4>🔍 SEO Automation Basic</h4>
                    <p>SERP tracking, análise de concorrentes, schema markup generator</p>
                </div>
                <div class="coming-item">
                    <h4>📱 Social Media Basic</h4>
                    <p>Multi-platform posting, hashtag trends, engagement analytics</p>
                </div>
                <div class="coming-item">
                    <h4>📧 Email Marketing Basic</h4>
                    <p>List validation, A/B testing, smart segmentation</p>
                </div>
                <div class="coming-item">
                    <h4>⚡ Automation Flows Basic</h4>
                    <p>CRM sync, lead scoring, pipeline optimization</p>
                </div>
                <div class="coming-item">
                    <h4>🎯 Pixel Tracking Basic</h4>
                    <p>Script de pixel para agente de IA rastrear novos leads</p>
                </div>
            </div>
        </div>

        <footer class="footer">
            <p>© 2025 <a href="https://assessorcaiomartins.com/" style="color: #1E9E16; text-decoration: none;" target="_blank">Assessor Caio Martins Directory</a> | Feito com 💚 para a comunidade de marketing</p>
            <p>Scripts documentados e testados para implementação segura</p>
        </footer>
    </div>
</body>
</html>
