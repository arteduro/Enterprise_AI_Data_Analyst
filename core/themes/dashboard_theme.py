"""
core/themes/dashboard_theme.py

Tema visual para dashboards HTML.

Autor: Edgar Arteaga
"""


class DashboardTheme:
    """
    Define el tema visual del dashboard.
    """

    @staticmethod
    def css() -> str:
        """
        Devuelve el CSS del dashboard.
        """

        return """
*{
    box-sizing:border-box;
    margin:0;
    padding:0;
}

body{
    background:#eef2f7;
    font-family:Segoe UI,Arial,sans-serif;
    color:#222;
    padding:35px;
}

.container{
    max-width:1600px;
    margin:auto;
}

header{
    background:white;
    padding:25px;
    border-radius:14px;
    box-shadow:0 6px 20px rgba(0,0,0,.08);
    margin-bottom:30px;
}

header h1{
    font-size:34px;
    margin-bottom:10px;
    color:#1f2937;
}

header p{
    font-size:16px;
    color:#666;
}

.dashboard-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(700px,1fr));
    gap:25px;
}

.card{
    background:white;
    padding:20px;
    border-radius:14px;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    overflow:hidden;
}

footer{
    margin-top:40px;
    text-align:center;
    color:#777;
    font-size:14px;
}
""".strip()