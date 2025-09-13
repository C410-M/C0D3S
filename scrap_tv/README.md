<div align="center">
  <h1>📡 API · Endpoints e Deploy</h1>
  <p>Documentação rápida da API + guia de deploy via Portainer</p>
</div>

<h2>🔗 Endpoints</h2>

<table>
  <thead>
    <tr>
      <th>Método</th>
      <th>Endpoint</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>GET</code></td>
      <td><code>/programacao/semana</code></td>
      <td>Toda programação da semana</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/programacao/hoje</code></td>
      <td>Apenas hoje</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/programacao/dia/terça</code></td>
      <td>Dia específico por nome</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/programacao/dia/10/09/2024</code></td>
      <td>Dia específico por data</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/programacao/estatisticas</code></td>
      <td>Estatísticas da programação</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/programacao/buscar?q=jornal&dia=segunda</code></td>
      <td>Busca com filtro (q, dia)</td>
    </tr>
  </tbody>
</table>

<h2>⚙️ Deploy via Portainer</h2>

<ol>
  <li>
    <strong>Faça commit</strong> do 
    <code>Dockerfile</code>, <code>docker-compose.yml</code>, <code>app.py</code>, 
    <code>requirements.txt</code> em um repositório (GitHub/GitLab).
  </li>
  <li>
    No <strong>Portainer</strong> → <em>Stacks</em> → <code>Add stack</code> → 
    <code>From Git repository</code> → informe <code>repo + branch</code>.
  </li>
  <li>
    O Portainer vai clonar e <strong>buildar a imagem</strong> conforme 
    <code>build: .</code> no <code>docker-compose.yml</code>.
  </li>
  <li>
    Depois do deploy, <strong>verifique logs</strong> e o <strong>healthcheck</strong> 
    no Portainer.
  </li>
</ol>
