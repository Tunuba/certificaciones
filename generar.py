import os, html, sys
from PIL import Image

RAIZ = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
C = 'certificados'

grupos = [
    ('Project Management Institute', [
        ('pmi-ia-generativa-aplicada.png', 'certificados/pmi-ia-generativa-aplicada.pdf', 'Practical Application of Generative AI for Project Managers', '12 de octubre de 2026', None),
        ('pmi-kickoff-agile.png', None, 'Fundamentals of Agile Project Management (Kickoff Agile)', '14 de septiembre de 2026', 'Insignia en Credly'),
        ('pmi-introduccion-pmp.png', None, 'Free Introduction, Project Management Professional (PMP)', '14 de septiembre de 2026', None),
        ('pmi-prompt-engineering.png', None, 'Talking to AI, Prompt Engineering for Project Managers', '14 de septiembre de 2026', None),
        ('pmi-kickoff-predictivo.png', 'https://www.credly.com/badges/35e8188c-e267-4866-9a4a-dcd12ef54228', 'Fundamentos de la Dirección de Proyectos Predictivos (Kickoff Predictive)', '29 de julio de 2026', 'Insignia en Credly'),
        ('pmi-ia-generativa-overview.png', None, 'Generative AI Overview for Project Managers', '29 de julio de 2026', None),
    ]),
    ('Atlassian', [
        ('atlassian-jira.png', 'certificados/atlassian-jira.pdf', 'Get the most out of Jira', '12 de octubre de 2026', None),
        ('atlassian-trello.png', 'certificados/atlassian-trello.pdf', 'Get the most out of Trello', '12 de octubre de 2026', None),
        ('atlassian-practicas-agiles.png', None, 'Apply agile practices to manage your work', '14 de septiembre de 2026', None),
    ]),
    ('Agile Academy', [
        ('agile-academy-agile-fundamentals.png', None, 'Agile Fundamentals', '12 de octubre de 2026', '4 horas'),
    ]),
    ('Simplilearn', [
        ('simplilearn-prince2.png', None, 'Introduction to PRINCE2', '14 de septiembre de 2026', None),
    ]),
    ('IBM SkillsBuild', [
        ('ibm-ciclo-vida-proyectos.png', None, 'Navegación por el ciclo de vida de la gestión de proyectos', '14 de septiembre de 2026', '4 horas 30 minutos'),
        ('ibm-muestra-agile.png', None, 'Módulo 1, Una muestra de Agile', '14 de septiembre de 2026', '3 horas'),
        ('ibm-presentacion-efectiva.png', None, 'Effective Presentation and Communication', '17 de agosto de 2026', '1 hora 30 minutos'),
        ('ibm-pensamiento-critico.png', None, 'Problem Solving and Critical Thinking', '16 de agosto de 2026', '1 hora 30 minutos'),
        ('ibm-colaboracion-equipo.png', None, 'Collaboration and Team Dynamics', '13 de agosto de 2026', '2 horas'),
        ('ibm-conceptos-gestion-proyectos.png', None, 'Exploración de los conceptos básicos de la gestión de proyectos', '12 de agosto de 2026', '2 horas 15 minutos'),
        ('ibm-comunicacion-interpersonal.png', None, 'Interpersonal and Workplace Communication', '12 de agosto de 2026', '1 hora 30 minutos'),
    ]),
    ('Cisco Networking Academy', [
        ('cisco-involucrando-actores.png', None, 'Involucrando a los actores para el éxito', '16 de agosto de 2026', None),
        ('cisco-informes-convincentes.png', None, 'Creación de informes convincentes', '16 de agosto de 2026', None),
    ]),
]

total = sum(len(g[1]) for g in grupos)
e = html.escape

CORTO = {'Project Management Institute': 'PMI', 'Cisco Networking Academy': 'Cisco'}
tarjetas = []
for nombre, items in grupos:
    for img, enlace, titulo, fecha, nota in items:
        w, h = Image.open(os.path.join(RAIZ, C, img)).size
        href = enlace or (C + '/' + img)
        if enlace and enlace.endswith('.pdf'):
            accion = 'Abrir PDF original'
        elif enlace:
            accion = 'Verificar en Credly'
        else:
            accion = 'Ver completo'
        clase = 'cert insignia' if 'kickoff' in img else 'cert'
        extra = f'<span>{e(nota)}</span>' if nota else ''
        tarjetas.append(
            f'      <a class="{clase}" href="{e(href)}" target="_blank" rel="noopener" '
            f'data-img="{C}/{img}" data-orig="{e(enlace or "")}" data-accion="{accion}">\n'
            f'        <div class="marco"><img src="{C}/{img}" width="{w}" height="{h}" loading="lazy" alt="{e(titulo)}"></div>\n'
            f'        <div class="texto"><b class="inst">{e(CORTO.get(nombre, nombre))}</b><strong>{e(titulo)}</strong>'
            f'<span>{fecha}</span>{extra}<em>{accion}</em></div>\n'
            f'      </a>')
secciones = ['  <section>\n    <div class="grid">\n' + '\n'.join(tarjetas) + '\n    </div>\n  </section>']

css = """
  :root {
    --cobalto:#16337A; --tinta:#0E1A33; --pizarra:#4A5670; --fondo:#EEF1F5; --papel:#FFFFFF; --linea:#D5DBE5;
    --ambar:#FFB21A; --rojo:#E0303F; --azul:#2266E8;
    --titulo:"Bricolage Grotesque", "Segoe UI", sans-serif; --texto:"Instrument Sans", "Segoe UI", sans-serif;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  html { scroll-behavior:smooth; }
  body { font-family:var(--texto); font-size:17px; line-height:1.6; background:var(--fondo); color:var(--tinta); }
  a { color:inherit; }
  :focus-visible { outline:3px solid var(--ambar); outline-offset:3px; border-radius:4px; }
  .ancho { max-width:1200px; margin:0 auto; padding:0 24px; }
  header { background:var(--cobalto); color:#fff; position:relative; }
  header::before { content:""; position:absolute; inset:0; pointer-events:none; opacity:.55;
    background:radial-gradient(circle at 1px 1px, rgba(255,255,255,.10) 1.2px, transparent 1.6px) 0 0/22px 22px; }
  header .ancho { position:relative; padding-top:40px; padding-bottom:34px; }
  header h1 { font-family:var(--titulo); font-weight:800; font-size:clamp(36px,5.4vw,76px); line-height:.95; letter-spacing:-.02em;
              font-variation-settings:"wdth" 92; }
  header .quien { margin-top:18px; font-size:19px; color:#DCE5FA; max-width:56ch; }
  header nav { margin-top:24px; display:flex; flex-wrap:wrap; gap:10px 22px; font-size:16px; }
  header nav a { color:#fff; text-decoration-color:rgba(255,178,26,.7); text-decoration-thickness:2px; text-underline-offset:5px; }
  header nav a:hover { color:var(--ambar); }
  main { padding-bottom:40px; }
  section { padding-top:28px; scroll-margin-top:8px; }
  h2 { font-family:var(--titulo); font-weight:800; font-size:clamp(22px,2.6vw,30px); letter-spacing:-.02em; line-height:1.05;
       display:flex; align-items:flex-end; gap:14px; margin-bottom:12px; }
  h2 small { font-family:var(--texto); font-weight:400; font-size:16px; color:var(--pizarra); letter-spacing:0; }
  h2::after { content:""; flex:1; height:4px; margin-bottom:8px; border-radius:2px;
    background:var(--linea); }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(min(196px,100%),1fr)); gap:12px; }
  .cert, .marco, .texto { min-width:0; }
  .cert { display:flex; flex-direction:column; background:var(--papel); border:1px solid var(--linea); border-radius:12px; overflow:hidden;
          text-decoration:none; color:inherit; transition:box-shadow .2s, border-color .2s; }
  .cert:hover { border-color:var(--cobalto); box-shadow:0 18px 40px -22px rgba(14,26,51,.55); }
  .marco { background:var(--tinta); padding:7px; display:flex; align-items:center; justify-content:center; aspect-ratio:3/2; }
  .marco { overflow:hidden; }
  .marco img { width:100%; height:100%; object-fit:contain; display:block; }
  .insignia .marco img { width:auto; height:84%; aspect-ratio:1; border-radius:50%; }
  .texto { padding:9px 11px 11px; display:flex; flex-direction:column; gap:1px; flex:1; }
  .texto .inst { font-family:var(--texto); font-size:11.5px; font-weight:600; color:var(--cobalto); }
  .texto strong { font-family:var(--titulo); font-weight:700; font-size:14px; line-height:1.25; letter-spacing:-.005em; }
  .texto span { font-size:12.5px; color:var(--pizarra); }
  .texto em { font-style:normal; font-size:12.5px; font-weight:600; color:var(--cobalto); margin-top:auto; padding-top:6px;
              text-decoration:underline; text-decoration-color:var(--ambar); text-decoration-thickness:2px; text-underline-offset:4px; }
  footer { margin-top:40px; background:var(--tinta); color:#C9D3E6; }
  footer .ancho { padding-top:36px; padding-bottom:40px; display:flex; flex-wrap:wrap; gap:12px 32px; justify-content:space-between; align-items:baseline; }
  footer strong { font-family:var(--titulo); color:#fff; font-size:22px; }
  footer a { color:#fff; text-underline-offset:4px; }
  .visor { position:fixed; inset:0; z-index:20; background:rgba(8,14,30,.94); display:none; flex-direction:column;
           align-items:center; justify-content:center; gap:14px; padding:60px 76px 28px; }
  .visor.abierto { display:flex; }
  .visor img { max-width:100%; max-height:calc(100vh - 170px); object-fit:contain; border-radius:6px; background:#fff;
               box-shadow:0 20px 60px rgba(0,0,0,.6); }
  .visor .pie { color:#C9D3E6; font-size:15px; text-align:center; max-width:70ch; }
  .visor .pie b { display:block; color:#fff; font-family:var(--titulo); font-size:19px; font-weight:700; }
  .visor .orig { background:var(--ambar); color:var(--tinta); font-weight:700; text-decoration:none; padding:9px 18px; border-radius:8px; }
  .visor .orig[hidden] { display:none; }
  .visor button { position:absolute; width:52px; height:52px; border-radius:50%; border:0; cursor:pointer;
                  background:rgba(255,255,255,.10); color:#fff; font-size:26px; line-height:1; }
  .visor button:hover { background:rgba(255,255,255,.22); }
  .visor .cerrar { top:14px; right:16px; font-size:22px; }
  .visor .ant { left:14px; top:50%; transform:translateY(-50%); }
  .visor .sig { right:14px; top:50%; transform:translateY(-50%); }
  @media (max-width:700px) { .visor { padding:64px 10px 20px; } .visor .ant, .visor .sig { display:none; } }
  @media (max-width:700px) { body { font-size:16px; } .ancho { padding:0 16px; } header .ancho { padding-top:44px; padding-bottom:36px; } }
"""

VISOR = r"""<div class="visor" role="dialog" aria-modal="true" aria-label="Certificado en grande">
  <img alt="">
  <div class="pie" aria-live="polite"></div>
  <a class="orig" target="_blank" rel="noopener" hidden></a>
  <button type="button" class="cerrar" aria-label="Cerrar">&#x2715;</button>
  <button type="button" class="ant" aria-label="Anterior">&#x2039;</button>
  <button type="button" class="sig" aria-label="Siguiente">&#x203A;</button>
</div>
<script>
(function () {
  var visor = document.querySelector('.visor'), foto = visor.querySelector('img'), pie = visor.querySelector('.pie'),
      orig = visor.querySelector('.orig'), certs = Array.prototype.slice.call(document.querySelectorAll('.cert')),
      pos = 0, origen = null;
  function mostrar() {
    var c = certs[pos], titulo = c.querySelector('strong').textContent;
    foto.src = c.dataset.img; foto.alt = titulo;
    pie.innerHTML = '';
    var b = document.createElement('b'); b.textContent = titulo; pie.appendChild(b);
    pie.appendChild(document.createTextNode(c.querySelector('.inst').textContent + ', ' + c.querySelector('span').textContent + '. ' + (pos + 1) + ' de ' + certs.length));
    if (c.dataset.orig) { orig.hidden = false; orig.href = c.dataset.orig; orig.textContent = c.dataset.accion; }
    else { orig.hidden = true; }
  }
  function abrir(i, el) { pos = i; origen = el; mostrar(); visor.classList.add('abierto'); document.body.style.overflow = 'hidden'; visor.querySelector('.cerrar').focus(); }
  function cerrar() { visor.classList.remove('abierto'); document.body.style.overflow = ''; if (origen) origen.focus(); }
  function mover(d) { pos = (pos + d + certs.length) % certs.length; mostrar(); }
  certs.forEach(function (c, i) {
    c.addEventListener('click', function (ev) {
      if (ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.button === 1) return;
      ev.preventDefault(); abrir(i, c);
    });
  });
  visor.querySelector('.cerrar').addEventListener('click', cerrar);
  visor.querySelector('.ant').addEventListener('click', function () { mover(-1); });
  visor.querySelector('.sig').addEventListener('click', function () { mover(1); });
  visor.addEventListener('click', function (ev) { if (ev.target === visor || ev.target === pie) cerrar(); });
  document.addEventListener('keydown', function (ev) {
    if (!visor.classList.contains('abierto')) return;
    if (ev.key === 'Escape') cerrar();
    else if (ev.key === 'ArrowLeft') mover(-1);
    else if (ev.key === 'ArrowRight') mover(1);
  });
  var x0 = null;
  visor.addEventListener('touchstart', function (ev) { x0 = ev.touches[0].clientX; }, { passive: true });
  visor.addEventListener('touchend', function (ev) {
    if (x0 === null) return; var dx = ev.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 45) mover(dx < 0 ? 1 : -1);
  });
})();
</script>
"""

pagina = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#16337A">
<title>Certificaciones de José Manuel González Corado</title>
<meta name="description" content="Soy José Manuel González Corado y estos son mis certificados en gestión de proyectos, métodos ágiles, IA generativa y trabajo en equipo.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wdth,wght@75..100,400..700&family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<header>
  <div class="ancho">
    <h1>Certificaciones</h1>
    <p class="quien">Tengo {total} certificados de PMI, IBM, Atlassian, Cisco, Agile Academy y Simplilearn, en gestión de proyectos, métodos ágiles, IA generativa y trabajo en equipo. Toca uno para verlo en grande.</p>
  </div>
</header>
<main class="ancho">
{chr(10).join(secciones)}
</main>
<footer>
  <div class="ancho">
    <strong>José Manuel González Corado</strong>
    <span>Mira mis proyectos en <a href="https://tunuba.github.io/proyectos/">tunuba.github.io/proyectos</a></span>
  </div>
</footer>
{VISOR}
</body>
</html>
"""

with open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(pagina)
with open(os.path.join(RAIZ, 'README.md'), 'w', encoding='utf-8') as f:
    f.write('# Certificaciones\n\nMis certificados, de José Manuel González Corado.\n\nVerlos en https://tunuba.github.io/certificaciones/\n')
print(total)
