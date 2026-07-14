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

    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    color:#222;

    padding:35px;

}

.container{

    max-width:1700px;

    margin:auto;

}


/* ========================================= */
/* HEADER ENTERPRISE                         */
/* ========================================= */

.dashboard-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:30px;

    background:#1f2937;

    color:white;

    border-radius:16px;

    margin-bottom:35px;

    box-shadow:
        0 12px 30px rgba(0,0,0,.15);

}

.dashboard-header h1{

    margin:0;

    font-size:34px;

    font-weight:700;

}

.dashboard-header p{

    margin-top:10px;

    color:#d1d5db;

    font-size:17px;

}

.header-info{

    text-align:right;

    font-size:14px;

    color:#d1d5db;

    line-height:1.7;

}


/* ========================================= */
/* GRID                                      */
/* ========================================= */

.dashboard-grid{

    display:grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(700px,1fr)
        );

    gap:30px;

}


/* ========================================= */
/* TARJETAS                                  */
/* ========================================= */

.card{

    background:white;

    padding:20px;

    border-radius:18px;

    box-shadow:

        0 10px 25px rgba(0,0,0,.08);

    transition:

        transform .25s ease,

        box-shadow .25s ease;

    overflow:hidden;

}

.card:hover{

    transform:translateY(-5px);

    box-shadow:

        0 18px 35px rgba(0,0,0,.12);

}


/* ========================================= */
/* PLOTLY                                    */
/* ========================================= */

.plotly-graph-div{

    width:100% !important;

}


/* ========================================= */
/* FOOTER                                    */
/* ========================================= */

footer{

    margin-top:45px;

    text-align:center;

    color:#6b7280;

    font-size:14px;

    padding:20px;

}


/* ========================================= */
/* RESPONSIVE                                */
/* ========================================= */

@media (max-width:1100px){

    .dashboard-header{

        flex-direction:column;

        align-items:flex-start;

        gap:20px;

    }

    .header-info{

        text-align:left;

    }

    .dashboard-grid{

        grid-template-columns:1fr;

    }

}
""".strip()