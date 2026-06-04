import streamlit as st

from utils.html import render_html


FRIENDS = [
    {
        "name": "LunaForge",
        "class": "Ward Mystic",
        "status": "Online",
        "streak": 18,
        "level": 12,
        "initials": "LF",
    },
    {
        "name": "IronTheo",
        "class": "Bulwark Knight",
        "status": "In Quest",
        "streak": 9,
        "level": 10,
        "initials": "IT",
    },
    {
        "name": "NovaVale",
        "class": "Hope Alchemist",
        "status": "Online",
        "streak": 14,
        "level": 11,
        "initials": "NV",
    },
    {
        "name": "MiraShade",
        "class": "Night Scout",
        "status": "Offline",
        "streak": 6,
        "level": 7,
        "initials": "MS",
    },
    {
        "name": "CinderKai",
        "class": "Ember Monk",
        "status": "Online",
        "streak": 21,
        "level": 15,
        "initials": "CK",
    },
]

CHALLENGES = [
    {
        "title": "Party Streak Pact",
        "progress": 76,
        "goal": "Maintain 5 active streaks for the week.",
        "reward": "+1,000 Hope Energy",
        "members": "5/5 joined",
    },
    {
        "title": "Outer Ward Relay",
        "progress": 58,
        "goal": "Complete 40 combined exercise sessions.",
        "reward": "Guild Lantern badge",
        "members": "4/6 joined",
    },
    {
        "title": "Boss Gate Warmup",
        "progress": 32,
        "goal": "Log 120 collective mobility minutes.",
        "reward": "+450 Party XP",
        "members": "3/5 joined",
    },
]


def _inject_friends_css():
    render_html(
        """
        <style>
            :root {
                --spire-purple: #7C3AED;
                --spire-dark: #1A1A1A;
                --spire-light: #E5E5E5;
                --spire-border: rgba(229, 229, 229, 0.13);
                --spire-muted: rgba(229, 229, 229, 0.66);
                --status-online: #47F0A3;
                --status-quest: #F5C542;
                --status-offline: #7A7A7A;
            }

            .stApp {
                background:
                    radial-gradient(circle at 14% 0%, rgba(124, 58, 237, 0.24), transparent 30rem),
                    radial-gradient(circle at 90% 10%, rgba(229, 229, 229, 0.08), transparent 22rem),
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

            .friends-shell {
                color: var(--spire-light);
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .friends-hero {
                border: 1px solid rgba(124, 58, 237, 0.4);
                border-radius: 8px;
                padding: 1.55rem;
                background:
                    linear-gradient(110deg, rgba(26, 26, 26, 0.96), rgba(35, 33, 41, 0.88)),
                    url("https://images.unsplash.com/photo-1535223289827-42f1e9919769?auto=format&fit=crop&w=1600&q=80");
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

            .friends-hero h1 {
                max-width: 780px;
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

            .social-grid {
                display: grid;
                grid-template-columns: minmax(0, 1.1fr) minmax(320px, 0.9fr);
                gap: 1rem;
                margin-top: 1rem;
            }

            .section-title {
                margin: 1.55rem 0 0.8rem;
                color: #FFFFFF;
                font-size: 1rem;
                font-weight: 850;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .friend-list,
            .challenge-stack {
                display: grid;
                gap: 0.8rem;
            }

            .friend-card,
            .challenge-card,
            .party-card {
                border: 1px solid var(--spire-border);
                border-radius: 8px;
                background: linear-gradient(145deg, rgba(45, 41, 54, 0.96), rgba(26, 26, 26, 0.96));
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28);
            }

            .friend-card {
                display: grid;
                grid-template-columns: auto minmax(0, 1fr) auto;
                align-items: center;
                gap: 1rem;
                padding: 1rem;
            }

            .avatar {
                position: relative;
                display: grid;
                place-items: center;
                width: 58px;
                height: 58px;
                border: 1px solid rgba(124, 58, 237, 0.62);
                border-radius: 8px;
                background:
                    radial-gradient(circle at 30% 25%, rgba(181, 140, 255, 0.5), rgba(124, 58, 237, 0.26) 45%, rgba(26, 26, 26, 0.9) 76%);
                color: #FFFFFF;
                font-weight: 900;
                box-shadow: 0 0 26px rgba(124, 58, 237, 0.28);
            }

            .status-dot {
                position: absolute;
                right: -4px;
                bottom: -4px;
                width: 15px;
                height: 15px;
                border: 2px solid #1A1A1A;
                border-radius: 50%;
                background: var(--status-offline);
            }

            .status-dot.online {
                background: var(--status-online);
                box-shadow: 0 0 16px rgba(71, 240, 163, 0.68);
            }

            .status-dot.quest {
                background: var(--status-quest);
                box-shadow: 0 0 16px rgba(245, 197, 66, 0.62);
            }

            .friend-name {
                color: #FFFFFF;
                font-size: 1.1rem;
                font-weight: 850;
            }

            .friend-class,
            .friend-meta,
            .challenge-copy,
            .party-copy {
                color: var(--spire-muted);
                line-height: 1.5;
            }

            .friend-meta {
                display: flex;
                flex-wrap: wrap;
                gap: 0.6rem;
                margin-top: 0.4rem;
                font-size: 0.86rem;
            }

            .friend-streak {
                min-width: 88px;
                text-align: right;
            }

            .streak-value {
                color: #FFFFFF;
                font-size: 1.8rem;
                font-weight: 900;
                line-height: 1;
            }

            .streak-label {
                margin-top: 0.25rem;
                color: var(--spire-muted);
                font-size: 0.74rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .challenge-card,
            .party-card {
                padding: 1rem;
            }

            .challenge-top,
            .party-top {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                gap: 1rem;
            }

            .challenge-title,
            .party-title {
                color: #FFFFFF;
                font-size: 1.08rem;
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
                font-weight: 800;
                white-space: nowrap;
            }

            .challenge-copy {
                margin-top: 0.65rem;
            }

            .progress-track {
                width: 100%;
                height: 16px;
                overflow: hidden;
                margin-top: 0.9rem;
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

            .challenge-footer {
                display: flex;
                justify-content: space-between;
                gap: 1rem;
                margin-top: 0.65rem;
                color: rgba(229, 229, 229, 0.72);
                font-size: 0.84rem;
                font-weight: 720;
            }

            .party-card {
                margin-top: 1rem;
                border-color: rgba(124, 58, 237, 0.46);
                box-shadow:
                    0 18px 44px rgba(0, 0, 0, 0.32),
                    0 0 34px rgba(124, 58, 237, 0.2);
            }

            @media (max-width: 900px) {
                .social-grid {
                    grid-template-columns: 1fr;
                }

                .friend-card {
                    grid-template-columns: auto minmax(0, 1fr);
                }

                .friend-streak {
                    grid-column: 1 / -1;
                    text-align: left;
                }
            }
        </style>
        """,
    )


def _status_class(status):
    if status == "Online":
        return "online"
    if status == "In Quest":
        return "quest"
    return "offline"


def _friend_card(friend):
    initials = friend["initials"]
    status = friend["status"]
    status_class = _status_class(status)
    name = friend["name"]
    player_class = friend["class"]
    level = friend["level"]
    streak = friend["streak"]

    return f"""
        <article class="friend-card">
            <div class="avatar">
                {initials}
                <span class="status-dot {status_class}"></span>
            </div>
            <div>
                <div class="friend-name">{name}</div>
                <div class="friend-class">{player_class}</div>
                <div class="friend-meta">
                    <span>{status}</span>
                    <span>Level {level}</span>
                </div>
            </div>
            <div class="friend-streak">
                <div class="streak-value">{streak}</div>
                <div class="streak-label">Day streak</div>
            </div>
        </article>
    """


def _challenge_card(challenge):
    title = challenge["title"]
    progress = challenge["progress"]
    goal = challenge["goal"]
    reward = challenge["reward"]
    members = challenge["members"]

    return f"""
        <article class="challenge-card">
            <div class="challenge-top">
                <div class="challenge-title">{title}</div>
                <div class="tag">{members}</div>
            </div>
            <div class="challenge-copy">{goal}</div>
            <div class="progress-track">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
            <div class="challenge-footer">
                <span>{progress}% complete</span>
                <span>{reward}</span>
            </div>
        </article>
    """


def show_friends():
    _inject_friends_css()

    online_count = sum(friend["status"] == "Online" for friend in FRIENDS)
    total_streaks = sum(friend["streak"] for friend in FRIENDS)
    friend_cards = "".join(_friend_card(friend) for friend in FRIENDS)
    challenge_cards = "".join(_challenge_card(challenge) for challenge in CHALLENGES)

    render_html(
        f"""
        <main class="friends-shell">
            <section class="friends-hero">
                <div class="eyebrow">SPIRE Friends // Guild Hall</div>
                <h1>Your party is gathering for the next run.</h1>
                <p class="hero-copy">
                    See who is online, compare streaks, and join cooperative challenges
                    that turn daily exercise into shared progress.
                </p>
            </section>

            <section class="social-grid">
                <div>
                    <div class="section-title">Friends List</div>
                    <div class="friend-list">
                        {friend_cards}
                    </div>
                </div>

                <aside>
                    <div class="section-title">Party Status</div>
                    <article class="party-card">
                        <div class="party-top">
                            <div>
                                <div class="eyebrow">Guild Pulse</div>
                                <div class="party-title">{online_count} allies online</div>
                            </div>
                            <div class="tag">{total_streaks} streak days</div>
                        </div>
                        <div class="party-copy">
                            Your circle is strongest in the evening window. Start a co-op run
                            while active players are still in the hall.
                        </div>
                    </article>

                    <div class="section-title">Cooperative Challenges</div>
                    <div class="challenge-stack">
                        {challenge_cards}
                    </div>
                </aside>
            </section>
        </main>
        """,
    )


show_friends()
