from base64 import b64encode
from pathlib import Path

from data.player_data import player
from utils.html import render_html


QUEST_PROGRESS = 73
COMMUNITY_PROGRESS = 68
HOPE_PROGRESS = 82
HERO_IMAGE = Path(__file__).parent / "assets" / "background" / "spireidil.jpeg"


def _fmt_number(value):
    return f"{value:,}"


def _image_data_uri(path):
    return f"data:image/jpeg;base64,{b64encode(path.read_bytes()).decode('ascii')}"


def _inject_home_css():
    hero_image_uri = _image_data_uri(HERO_IMAGE)

    css = """
        <style>
            :root {
                --spire-purple: #7C3AED;
                --spire-dark: #1A1A1A;
                --spire-light: #E5E5E5;
                --spire-panel: #232129;
                --spire-panel-strong: #2D2936;
                --spire-border: rgba(229, 229, 229, 0.12);
                --spire-muted: rgba(229, 229, 229, 0.68);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(124, 58, 237, 0.24), transparent 32rem),
                    radial-gradient(circle at 82% 18%, rgba(229, 229, 229, 0.08), transparent 24rem),
                    var(--spire-dark);
                color: var(--spire-light);
            }

            [data-testid="stHeader"] {
                background: transparent;
            }

            .block-container {
                max-width: 1180px;
                padding-top: 2rem;
                padding-bottom: 3rem;
            }

            .home-shell {
                color: var(--spire-light);
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .hero-banner {
                min-height: 430px;
                display: flex;
                align-items: flex-end;
                overflow: hidden;
                border: 1px solid rgba(124, 58, 237, 0.42);
                border-radius: 8px;
                background:
                    linear-gradient(90deg, rgba(26, 26, 26, 0.94) 0%, rgba(26, 26, 26, 0.66) 42%, rgba(26, 26, 26, 0.18) 100%),
                    linear-gradient(0deg, rgba(26, 26, 26, 0.98), rgba(26, 26, 26, 0.08) 60%),
                    url("__HERO_IMAGE_URI__");
                background-position: center 42%;
                background-size: cover;
                box-shadow: 0 22px 70px rgba(0, 0, 0, 0.42);
            }

            .hero-content {
                width: min(710px, 100%);
                padding: 2.2rem;
            }

            .eyebrow {
                color: var(--spire-purple);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.12em;
                text-transform: uppercase;
            }

            .hero-title {
                margin: 0.45rem 0 0.8rem;
                color: #FFFFFF;
                font-size: clamp(2.45rem, 5vw, 4.8rem);
                font-weight: 900;
                line-height: 0.92;
                letter-spacing: 0;
            }

            .hero-copy {
                max-width: 620px;
                margin: 0;
                color: var(--spire-muted);
                font-size: 1.04rem;
                line-height: 1.6;
            }

            .section-title {
                margin: 1.55rem 0 0.8rem;
                color: #FFFFFF;
                font-size: 1rem;
                font-weight: 850;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .stats-grid {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 0.85rem;
                margin-top: 1rem;
            }

            .stat-card,
            .quest-card,
            .panel-card,
            .activity-card {
                border: 1px solid var(--spire-border);
                border-radius: 8px;
                background: linear-gradient(145deg, rgba(45, 41, 54, 0.96), rgba(26, 26, 26, 0.96));
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28);
            }

            .stat-card {
                position: relative;
                min-height: 122px;
                padding: 1rem;
                overflow: hidden;
            }

            .stat-card::before {
                content: "";
                position: absolute;
                inset: 0;
                border-top: 2px solid rgba(124, 58, 237, 0.7);
                pointer-events: none;
            }

            .stat-label {
                color: var(--spire-muted);
                font-size: 0.8rem;
                font-weight: 760;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            .stat-value {
                margin-top: 0.7rem;
                color: #FFFFFF;
                font-size: 2.3rem;
                font-weight: 900;
                line-height: 1;
            }

            .stat-note {
                margin-top: 0.55rem;
                color: rgba(229, 229, 229, 0.6);
                font-size: 0.86rem;
            }

            .dashboard-grid {
                display: grid;
                grid-template-columns: minmax(0, 1.45fr) minmax(300px, 0.75fr);
                gap: 1rem;
                margin-top: 1rem;
            }

            .quest-card {
                padding: 1.25rem;
            }

            .quest-top,
            .widget-top {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
            }

            .quest-name,
            .widget-title {
                color: #FFFFFF;
                font-size: 1.18rem;
                font-weight: 850;
            }

            .tag {
                flex: 0 0 auto;
                border: 1px solid rgba(124, 58, 237, 0.52);
                border-radius: 999px;
                padding: 0.25rem 0.65rem;
                background: rgba(124, 58, 237, 0.16);
                color: #D8C8FF;
                font-size: 0.76rem;
                font-weight: 760;
            }

            .quest-copy,
            .panel-copy,
            .activity-meta {
                color: var(--spire-muted);
                line-height: 1.5;
            }

            .quest-copy {
                margin: 0.7rem 0 1rem;
            }

            .progress-track {
                width: 100%;
                height: 18px;
                overflow: hidden;
                border: 1px solid rgba(229, 229, 229, 0.16);
                border-radius: 999px;
                background: rgba(229, 229, 229, 0.08);
            }

            .progress-fill {
                height: 100%;
                border-radius: 999px;
                background: linear-gradient(90deg, #7C3AED, #B58CFF);
                box-shadow: 0 0 28px rgba(124, 58, 237, 0.66);
            }

            .progress-label {
                display: flex;
                justify-content: space-between;
                margin-top: 0.6rem;
                color: rgba(229, 229, 229, 0.72);
                font-size: 0.86rem;
                font-weight: 720;
            }

            .activity-card {
                padding: 1rem 1.15rem;
                margin-bottom: 0.7rem;
            }

            .activity-title {
                color: #FFFFFF;
                font-weight: 800;
            }

            .side-stack {
                display: grid;
                gap: 1rem;
            }

            .panel-card {
                padding: 1.1rem;
            }

            .big-number {
                margin: 0.9rem 0 0.55rem;
                color: #FFFFFF;
                font-size: 2.05rem;
                font-weight: 900;
                line-height: 1;
            }

            .energy-core {
                display: grid;
                place-items: center;
                width: 142px;
                height: 142px;
                margin: 1rem auto 0.75rem;
                border: 1px solid rgba(124, 58, 237, 0.55);
                border-radius: 50%;
                background:
                    radial-gradient(circle, rgba(181, 140, 255, 0.36) 0%, rgba(124, 58, 237, 0.18) 45%, rgba(26, 26, 26, 0.92) 70%);
                box-shadow: 0 0 40px rgba(124, 58, 237, 0.38), inset 0 0 32px rgba(124, 58, 237, 0.3);
            }

            .energy-core span {
                color: #FFFFFF;
                font-size: 1.8rem;
                font-weight: 900;
            }

            @media (max-width: 900px) {
                .stats-grid,
                .dashboard-grid {
                    grid-template-columns: 1fr;
                }

                .hero-content {
                    padding: 1.45rem;
                }

                .hero-banner {
                    min-height: 420px;
                    background-position: center top;
                }
            }
        </style>
        """.replace("__HERO_IMAGE_URI__", hero_image_uri)

    render_html(css)


def show_home():
    _inject_home_css()

    render_html(
        f"""
        <main class="home-shell">
            <section class="hero-banner">
                <div class="hero-content">
                    <div class="eyebrow">SPIRE Companion // Nightfall Run</div>
                    <h1 class="hero-title">Welcome back, {player["name"]}</h1>
                    <p class="hero-copy">
                        The Workshop Dungeon is shifting again. Track your power, rally your party,
                        and turn every completed ritual into Hope Energy for the wider realm.
                    </p>
                </div>
            </section>

            <section class="stats-grid" aria-label="Player statistics">
                <article class="stat-card">
                    <div class="stat-label">Level</div>
                    <div class="stat-value">{player["level"]}</div>
                    <div class="stat-note">Shadow rank advancing</div>
                </article>
                <article class="stat-card">
                    <div class="stat-label">Streak</div>
                    <div class="stat-value">{player["streak"]}</div>
                    <div class="stat-note">Days without retreat</div>
                </article>
                <article class="stat-card">
                    <div class="stat-label">Achievements</div>
                    <div class="stat-value">{player["achievements"]}</div>
                    <div class="stat-note">Relics unlocked</div>
                </article>
                <article class="stat-card">
                    <div class="stat-label">Friends</div>
                    <div class="stat-value">{player["friends"]}</div>
                    <div class="stat-note">Allies in the keep</div>
                </article>
            </section>

            <section class="dashboard-grid">
                <div>
                    <div class="section-title">Current Quest</div>
                    <article class="quest-card">
                        <div class="quest-top">
                            <div class="quest-name">Escape the Workshop Dungeon</div>
                            <div class="tag">Act II</div>
                        </div>
                        <p class="quest-copy">
                            Complete today's exercise chain, restore your strength, and unlock the
                            next gate before the dungeon resets at midnight.
                        </p>
                        <div class="progress-track">
                            <div class="progress-fill" style="width: {QUEST_PROGRESS}%"></div>
                        </div>
                        <div class="progress-label">
                            <span>{QUEST_PROGRESS}% complete</span>
                            <span>27 XP to gate key</span>
                        </div>
                    </article>

                    <div class="section-title">Recent Activity</div>
                    <article class="activity-card">
                        <div class="activity-title">Forged a 12-day streak</div>
                        <div class="activity-meta">Daily focus ritual completed before dusk.</div>
                    </article>
                    <article class="activity-card">
                        <div class="activity-title">Unlocked Moonlit Resolve</div>
                        <div class="activity-meta">Achievement #{player["achievements"]} added to the relic vault.</div>
                    </article>
                    <article class="activity-card">
                        <div class="activity-title">Joined a party surge</div>
                        <div class="activity-meta">{player["friends"]} allies contributed progress to the community objective.</div>
                    </article>
                </div>

                <aside class="side-stack">
                    <div>
                        <div class="section-title">Community Goal</div>
                        <article class="panel-card">
                            <div class="widget-top">
                                <div class="widget-title">Light the Outer Ward</div>
                                <div class="tag">{COMMUNITY_PROGRESS}%</div>
                            </div>
                            <div class="big-number">34,200 / 50,000</div>
                            <div class="progress-track">
                                <div class="progress-fill" style="width: {COMMUNITY_PROGRESS}%"></div>
                            </div>
                            <p class="panel-copy">
                                Shared Hope Energy is pushing the ward toward its next charity unlock.
                            </p>
                        </article>
                    </div>

                    <div>
                        <div class="section-title">Hope Energy</div>
                        <article class="panel-card">
                            <div class="widget-top">
                                <div class="widget-title">Personal Core</div>
                                <div class="tag">Charged</div>
                            </div>
                            <div class="energy-core"><span>{HOPE_PROGRESS}%</span></div>
                            <div class="big-number">{_fmt_number(player["hope_energy"])}</div>
                            <p class="panel-copy">
                                Energy generated from quests, streaks, and ally actions.
                            </p>
                        </article>
                    </div>
                </aside>
            </section>
        </main>
        """,
    )
