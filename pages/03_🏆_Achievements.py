import streamlit as st

from utils.html import render_html


ACHIEVEMENTS = {
    "Progress": [
        {
            "name": "First Step Beyond the Gate",
            "description": "Complete your first exercise ritual.",
            "reward": "+50 XP",
            "unlocked": True,
        },
        {
            "name": "Dungeon Cartographer",
            "description": "Log 25 total exercise sessions.",
            "reward": "+150 XP",
            "unlocked": True,
        },
        {
            "name": "Ascendant Form",
            "description": "Reach level 10 in the SPIRE companion.",
            "reward": "Rare title",
            "unlocked": False,
        },
    ],
    "Consistency": [
        {
            "name": "Seven Flames",
            "description": "Keep a 7-day streak alive.",
            "reward": "+100 Hope",
            "unlocked": True,
        },
        {
            "name": "Moonlit Resolve",
            "description": "Complete 12 days without breaking your chain.",
            "reward": "+250 Hope",
            "unlocked": True,
        },
        {
            "name": "Unbroken Ward",
            "description": "Maintain a 30-day exercise streak.",
            "reward": "Epic frame",
            "unlocked": False,
        },
    ],
    "Community": [
        {
            "name": "Party Signal",
            "description": "Add your first friend to the keep.",
            "reward": "+75 XP",
            "unlocked": True,
        },
        {
            "name": "Raid Circle",
            "description": "Contribute to a community goal with 5 allies.",
            "reward": "+300 Hope",
            "unlocked": False,
        },
        {
            "name": "Guild Lantern",
            "description": "Help the community complete a weekly objective.",
            "reward": "Guild banner",
            "unlocked": False,
        },
    ],
    "Impact": [
        {
            "name": "Spark Bearer",
            "description": "Generate your first 1,000 Hope Energy.",
            "reward": "+100 XP",
            "unlocked": True,
        },
        {
            "name": "Outer Ward Keeper",
            "description": "Generate 10,000 total Hope Energy.",
            "reward": "+500 Hope",
            "unlocked": True,
        },
        {
            "name": "Beacon of the Realm",
            "description": "Help unlock a future charity milestone.",
            "reward": "Legendary aura",
            "unlocked": False,
        },
    ],
}


def _inject_achievements_css():
    render_html(
        """
        <style>
            :root {
                --spire-purple: #7C3AED;
                --spire-dark: #1A1A1A;
                --spire-light: #E5E5E5;
                --spire-border: rgba(229, 229, 229, 0.13);
                --spire-muted: rgba(229, 229, 229, 0.66);
            }

            .stApp {
                background:
                    radial-gradient(circle at 12% 0%, rgba(124, 58, 237, 0.24), transparent 30rem),
                    radial-gradient(circle at 86% 14%, rgba(229, 229, 229, 0.08), transparent 22rem),
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

            .achievements-shell {
                color: var(--spire-light);
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .achievements-hero {
                border: 1px solid rgba(124, 58, 237, 0.4);
                border-radius: 8px;
                padding: 1.55rem;
                background:
                    linear-gradient(110deg, rgba(26, 26, 26, 0.96), rgba(35, 33, 41, 0.88)),
                    url("https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1600&q=80");
                background-position: center;
                background-size: cover;
                box-shadow: 0 22px 70px rgba(0, 0, 0, 0.36);
            }

            .eyebrow {
                color: var(--spire-purple);
                font-size: 0.78rem;
                font-weight: 850;
                letter-spacing: 0.12em;
                text-transform: uppercase;
            }

            .achievements-hero h1 {
                max-width: 760px;
                margin: 0.35rem 0 0;
                color: #FFFFFF;
                font-size: clamp(2.1rem, 5vw, 4.2rem);
                font-weight: 900;
                line-height: 0.96;
                letter-spacing: 0;
            }

            .hero-copy {
                max-width: 720px;
                margin: 0.85rem 0 0;
                color: var(--spire-muted);
                font-size: 1.02rem;
                line-height: 1.6;
            }

            .summary-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.85rem;
                margin-top: 1rem;
            }

            .summary-card,
            .achievement-card {
                border: 1px solid var(--spire-border);
                border-radius: 8px;
                background: linear-gradient(145deg, rgba(45, 41, 54, 0.96), rgba(26, 26, 26, 0.96));
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28);
            }

            .summary-card {
                padding: 1rem;
            }

            .summary-label {
                color: var(--spire-muted);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .summary-value {
                margin-top: 0.65rem;
                color: #FFFFFF;
                font-size: 2.2rem;
                font-weight: 900;
                line-height: 1;
            }

            .category-title {
                margin: 1.65rem 0 0.85rem;
                color: #FFFFFF;
                font-size: 1rem;
                font-weight: 850;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .achievement-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.9rem;
            }

            .achievement-card {
                min-height: 190px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 1rem;
                position: relative;
                overflow: hidden;
            }

            .achievement-card.unlocked {
                border-color: rgba(124, 58, 237, 0.7);
                box-shadow:
                    0 18px 44px rgba(0, 0, 0, 0.32),
                    0 0 34px rgba(124, 58, 237, 0.34),
                    inset 0 0 26px rgba(124, 58, 237, 0.18);
            }

            .achievement-card.unlocked::before {
                content: "";
                position: absolute;
                inset: 0;
                border-top: 2px solid rgba(181, 140, 255, 0.9);
                pointer-events: none;
            }

            .achievement-card.locked {
                filter: grayscale(0.9);
                opacity: 0.52;
                background: linear-gradient(145deg, rgba(50, 50, 50, 0.8), rgba(26, 26, 26, 0.96));
            }

            .achievement-top {
                display: flex;
                align-items: flex-start;
                justify-content: space-between;
                gap: 0.85rem;
            }

            .achievement-icon {
                display: grid;
                place-items: center;
                width: 46px;
                height: 46px;
                flex: 0 0 auto;
                border: 1px solid rgba(124, 58, 237, 0.52);
                border-radius: 8px;
                background: rgba(124, 58, 237, 0.16);
                color: #FFFFFF;
                font-size: 1.35rem;
                font-weight: 900;
            }

            .achievement-card.locked .achievement-icon {
                border-color: rgba(229, 229, 229, 0.2);
                background: rgba(229, 229, 229, 0.08);
            }

            .achievement-status {
                border: 1px solid rgba(124, 58, 237, 0.52);
                border-radius: 999px;
                padding: 0.22rem 0.62rem;
                background: rgba(124, 58, 237, 0.16);
                color: #D8C8FF;
                font-size: 0.72rem;
                font-weight: 850;
                text-transform: uppercase;
                white-space: nowrap;
            }

            .achievement-card.locked .achievement-status {
                border-color: rgba(229, 229, 229, 0.18);
                background: rgba(229, 229, 229, 0.08);
                color: rgba(229, 229, 229, 0.72);
            }

            .achievement-name {
                margin-top: 0.9rem;
                color: #FFFFFF;
                font-size: 1.08rem;
                font-weight: 850;
                line-height: 1.25;
            }

            .achievement-description {
                margin-top: 0.5rem;
                color: var(--spire-muted);
                line-height: 1.5;
            }

            .achievement-reward {
                margin-top: 1rem;
                color: #D8C8FF;
                font-size: 0.82rem;
                font-weight: 850;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            @media (max-width: 900px) {
                .summary-grid,
                .achievement-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """,
    )


def _achievement_card(achievement):
    state = "unlocked" if achievement["unlocked"] else "locked"
    icon = "V" if achievement["unlocked"] else "X"
    status = "Unlocked" if achievement["unlocked"] else "Locked"

    return f"""
        <article class="achievement-card {state}">
            <div>
                <div class="achievement-top">
                    <div class="achievement-icon">{icon}</div>
                    <div class="achievement-status">{status}</div>
                </div>
                <div class="achievement-name">{achievement["name"]}</div>
                <div class="achievement-description">{achievement["description"]}</div>
            </div>
            <div class="achievement-reward">{achievement["reward"]}</div>
        </article>
    """


def show_achievements():
    _inject_achievements_css()

    all_achievements = [
        achievement
        for category_achievements in ACHIEVEMENTS.values()
        for achievement in category_achievements
    ]
    unlocked_count = sum(achievement["unlocked"] for achievement in all_achievements)
    locked_count = len(all_achievements) - unlocked_count
    completion_percentage = round((unlocked_count / len(all_achievements)) * 100)

    category_sections = ""
    for category, achievements in ACHIEVEMENTS.items():
        cards = "".join(_achievement_card(achievement) for achievement in achievements)
        category_sections += f"""
            <section>
                <div class="category-title">{category}</div>
                <div class="achievement-grid">{cards}</div>
            </section>
        """

    render_html(
        f"""
        <main class="achievements-shell">
            <section class="achievements-hero">
                <div class="eyebrow">SPIRE Achievements // Relic Vault</div>
                <h1>Collect proof of every victory.</h1>
                <p class="hero-copy">
                    Achievements mark your growth across training, consistency,
                    community action, and real impact. Unlocked relics burn purple;
                    hidden trials wait in ash-grey silence.
                </p>
            </section>

            <section class="summary-grid" aria-label="Achievement summary">
                <article class="summary-card">
                    <div class="summary-label">Unlocked</div>
                    <div class="summary-value">{unlocked_count}</div>
                </article>
                <article class="summary-card">
                    <div class="summary-label">Locked</div>
                    <div class="summary-value">{locked_count}</div>
                </article>
                <article class="summary-card">
                    <div class="summary-label">Vault Completion</div>
                    <div class="summary-value">{completion_percentage}%</div>
                </article>
            </section>

            {category_sections}
        </main>
        """,
    )


show_achievements()
