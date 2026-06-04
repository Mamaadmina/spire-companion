import streamlit as st

from utils.html import render_html


COMMUNITY_ENERGY = 125_000

MILESTONES = [
    {
        "title": "Campus Wellness Fund",
        "progress": 72,
        "target": "150,000 Hope Energy",
        "description": "Unlocks a proposed sponsor-funded donation to student wellbeing activities.",
    },
    {
        "title": "Local Health Partner",
        "progress": 48,
        "target": "250,000 Hope Energy",
        "description": "Represents a future pathway for supporting community health initiatives.",
    },
    {
        "title": "Accessibility Boost",
        "progress": 31,
        "target": "400,000 Hope Energy",
        "description": "Could help fund inclusive sport or rehabilitation resources through partners.",
    },
]

SPONSOR_EXAMPLES = [
    {
        "name": "Example Sponsor A",
        "model": "1,000 Hope Energy = EUR 1 pledged",
        "cap": "Monthly cap: EUR 500",
    },
    {
        "name": "Example Sponsor B",
        "model": "Community milestone unlocks a fixed donation",
        "cap": "Milestone pledge: EUR 250",
    },
    {
        "name": "Example Sponsor C",
        "model": "Weekly challenge completion funds a local cause",
        "cap": "Challenge pledge: EUR 100",
    },
]


def _inject_impact_css():
    render_html(
        """
        <style>
            :root {
                --spire-purple: #7C3AED;
                --spire-dark: #1A1A1A;
                --spire-light: #E5E5E5;
                --spire-border: rgba(229, 229, 229, 0.13);
                --spire-muted: rgba(229, 229, 229, 0.68);
            }

            .stApp {
                background:
                    radial-gradient(circle at 12% 0%, rgba(124, 58, 237, 0.24), transparent 30rem),
                    radial-gradient(circle at 86% 12%, rgba(229, 229, 229, 0.08), transparent 22rem),
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

            .impact-shell {
                color: var(--spire-light);
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .impact-hero {
                border: 1px solid rgba(124, 58, 237, 0.4);
                border-radius: 8px;
                padding: 1.55rem;
                background:
                    linear-gradient(110deg, rgba(26, 26, 26, 0.96), rgba(35, 33, 41, 0.86)),
                    url("https://images.unsplash.com/photo-1491438590914-bc09fcaaf77a?auto=format&fit=crop&w=1600&q=80");
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

            .impact-hero h1 {
                max-width: 800px;
                margin: 0.35rem 0 0;
                color: #FFFFFF;
                font-size: clamp(2.1rem, 5vw, 4.2rem);
                font-weight: 900;
                line-height: 0.96;
                letter-spacing: 0;
            }

            .hero-copy,
            .card-copy,
            .diagram-copy,
            .milestone-copy,
            .sponsor-copy {
                color: var(--spire-muted);
                line-height: 1.55;
            }

            .hero-copy {
                max-width: 780px;
                margin: 0.85rem 0 0;
                font-size: 1.02rem;
            }

            .section-title {
                margin: 1.55rem 0 0.8rem;
                color: #FFFFFF;
                font-size: 1rem;
                font-weight: 850;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .overview-grid,
            .sponsor-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.9rem;
                margin-top: 1rem;
            }

            .main-grid {
                display: grid;
                grid-template-columns: minmax(0, 1.1fr) minmax(320px, 0.9fr);
                gap: 1rem;
                margin-top: 1rem;
            }

            .impact-card,
            .diagram-card,
            .milestone-card,
            .sponsor-card,
            .explain-card {
                border: 1px solid var(--spire-border);
                border-radius: 8px;
                background: linear-gradient(145deg, rgba(45, 41, 54, 0.96), rgba(26, 26, 26, 0.96));
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28);
            }

            .impact-card,
            .sponsor-card,
            .explain-card {
                padding: 1rem;
            }

            .impact-value {
                margin-top: 0.65rem;
                color: #FFFFFF;
                font-size: 2.15rem;
                font-weight: 900;
                line-height: 1;
            }

            .card-title,
            .diagram-title,
            .milestone-title,
            .sponsor-title {
                color: #FFFFFF;
                font-size: 1.08rem;
                font-weight: 850;
            }

            .flow-diagram {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 0.7rem;
                margin-top: 0.9rem;
            }

            .diagram-card {
                min-height: 155px;
                padding: 1rem;
                position: relative;
                overflow: hidden;
            }

            .diagram-card::before {
                content: "";
                position: absolute;
                inset: 0;
                border-top: 2px solid rgba(124, 58, 237, 0.72);
                pointer-events: none;
            }

            .diagram-step {
                display: grid;
                place-items: center;
                width: 38px;
                height: 38px;
                margin-bottom: 0.75rem;
                border: 1px solid rgba(124, 58, 237, 0.58);
                border-radius: 50%;
                background: rgba(124, 58, 237, 0.18);
                color: #FFFFFF;
                font-weight: 900;
                box-shadow: 0 0 24px rgba(124, 58, 237, 0.28);
            }

            .milestone-stack {
                display: grid;
                gap: 0.8rem;
            }

            .milestone-card {
                padding: 1rem;
            }

            .milestone-top,
            .sponsor-top {
                display: flex;
                align-items: flex-start;
                justify-content: space-between;
                gap: 1rem;
            }

            .tag {
                flex: 0 0 auto;
                border: 1px solid rgba(124, 58, 237, 0.52);
                border-radius: 999px;
                padding: 0.25rem 0.65rem;
                background: rgba(124, 58, 237, 0.16);
                color: #D8C8FF;
                font-size: 0.76rem;
                font-weight: 800;
                white-space: nowrap;
            }

            .progress-track {
                width: 100%;
                height: 16px;
                overflow: hidden;
                margin-top: 0.85rem;
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

            .sponsor-copy {
                margin-top: 0.75rem;
            }

            .explain-list {
                display: grid;
                gap: 0.75rem;
                margin-top: 0.75rem;
            }

            .explain-item {
                border-left: 2px solid rgba(124, 58, 237, 0.78);
                padding-left: 0.85rem;
                color: var(--spire-muted);
                line-height: 1.5;
            }

            .explain-item strong {
                color: #FFFFFF;
            }

            @media (max-width: 900px) {
                .overview-grid,
                .sponsor-grid,
                .main-grid,
                .flow-diagram {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """,
    )


def _milestone_card(milestone):
    title = milestone["title"]
    progress = milestone["progress"]
    target = milestone["target"]
    description = milestone["description"]

    return f"""
        <article class="milestone-card">
            <div class="milestone-top">
                <div>
                    <div class="milestone-title">{title}</div>
                    <div class="milestone-copy">{target}</div>
                </div>
                <div class="tag">{progress}%</div>
            </div>
            <div class="progress-track">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
            <div class="milestone-copy" style="margin-top: 0.75rem;">{description}</div>
        </article>
    """


def _sponsor_card(sponsor):
    name = sponsor["name"]
    model = sponsor["model"]
    cap = sponsor["cap"]

    return f"""
        <article class="sponsor-card">
            <div class="sponsor-top">
                <div class="sponsor-title">{name}</div>
                <div class="tag">Example</div>
            </div>
            <div class="sponsor-copy">{model}</div>
            <div class="sponsor-copy">{cap}</div>
        </article>
    """


def show_impact():
    _inject_impact_css()

    milestone_cards = "".join(_milestone_card(milestone) for milestone in MILESTONES)
    sponsor_cards = "".join(_sponsor_card(sponsor) for sponsor in SPONSOR_EXAMPLES)

    render_html(
        f"""
        <main class="impact-shell">
            <section class="impact-hero">
                <div class="eyebrow">SPIRE Impact // Hope Energy Model</div>
                <h1>Turning exercise completion into visible social value.</h1>
                <p class="hero-copy">
                    Hope Energy is a concept layer for SPIRE: players complete exercise quests,
                    the app converts verified activity into a shared community score, and future
                    sponsors could use that score to trigger charitable contributions.
                </p>
            </section>

            <section class="overview-grid" aria-label="Hope Energy summary">
                <article class="impact-card">
                    <div class="eyebrow">Community Energy</div>
                    <div class="impact-value">{COMMUNITY_ENERGY:,}</div>
                    <div class="card-copy">Mock Hope Energy generated by the SPIRE community.</div>
                </article>
                <article class="impact-card">
                    <div class="eyebrow">Purpose</div>
                    <div class="impact-value">Motivation</div>
                    <div class="card-copy">Makes individual progress feel connected to something larger.</div>
                </article>
                <article class="impact-card">
                    <div class="eyebrow">Status</div>
                    <div class="impact-value">Concept</div>
                    <div class="card-copy">A prototype mechanism for assessment and future partner exploration.</div>
                </article>
            </section>

            <div class="section-title">Concept Diagram</div>
            <section class="flow-diagram" aria-label="Hope Energy flow diagram">
                <article class="diagram-card">
                    <div class="diagram-step">1</div>
                    <div class="diagram-title">Exercise Quest</div>
                    <div class="diagram-copy">A user completes a daily exercise session or streak challenge.</div>
                </article>
                <article class="diagram-card">
                    <div class="diagram-step">2</div>
                    <div class="diagram-title">Hope Energy</div>
                    <div class="diagram-copy">The app converts completion into a non-monetary community score.</div>
                </article>
                <article class="diagram-card">
                    <div class="diagram-step">3</div>
                    <div class="diagram-title">Community Goal</div>
                    <div class="diagram-copy">Players collectively fill milestone bars through repeated activity.</div>
                </article>
                <article class="diagram-card">
                    <div class="diagram-step">4</div>
                    <div class="diagram-title">Partner Action</div>
                    <div class="diagram-copy">A sponsor could translate milestones into pledged support for a cause.</div>
                </article>
            </section>

            <section class="main-grid">
                <div>
                    <div class="section-title">Milestone Progress</div>
                    <div class="milestone-stack">
                        {milestone_cards}
                    </div>
                </div>

                <aside>
                    <div class="section-title">How It Supports Charity</div>
                    <article class="explain-card">
                        <div class="card-title">Assessment framing</div>
                        <div class="explain-list">
                            <div class="explain-item"><strong>Behavior first:</strong> users are rewarded for completing healthy actions, not for donating money themselves.</div>
                            <div class="explain-item"><strong>Collective progress:</strong> many small exercise completions build toward shared goals that are easy to understand.</div>
                            <div class="explain-item"><strong>Sponsor bridge:</strong> external partners could pledge funds when agreed thresholds are reached.</div>
                            <div class="explain-item"><strong>Transparency:</strong> milestone targets, caps, and contribution rules should be visible before a campaign starts.</div>
                        </div>
                    </article>
                </aside>
            </section>

            <div class="section-title">Sponsor Contribution Examples</div>
            <section class="sponsor-grid">
                {sponsor_cards}
            </section>
        </main>
        """,
    )


show_impact()
