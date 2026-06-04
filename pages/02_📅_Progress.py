import calendar
from datetime import date, timedelta

import streamlit as st

from utils.html import render_html


MOCK_YEAR = 2026
MOCK_MONTH = 6

COMPLETED_DAYS = {
    1,
    2,
    3,
    5,
    6,
    7,
    8,
    9,
    12,
    13,
    14,
    15,
    16,
    17,
    20,
    21,
    22,
    23,
    26,
    27,
    28,
}

REMINDERS = [
    {
        "title": "Dawn Mobility Ritual",
        "time": "08:00",
        "copy": "A light session keeps the streak ward burning.",
    },
    {
        "title": "Evening Strength Quest",
        "time": "19:30",
        "copy": "Finish three exercise sets to claim today's XP.",
    },
    {
        "title": "Party Check-in",
        "time": "Sunday",
        "copy": "Share progress with allies before the weekly reset.",
    },
]


def _current_streak(completed_dates):
    if not completed_dates:
        return 0

    cursor = max(completed_dates)
    streak = 0
    while cursor in completed_dates:
        streak += 1
        cursor -= timedelta(days=1)

    return streak


def _longest_streak(completed_dates):
    longest = 0
    current = 0
    previous = None

    for completed_date in sorted(completed_dates):
        if previous and completed_date == previous + timedelta(days=1):
            current += 1
        else:
            current = 1

        longest = max(longest, current)
        previous = completed_date

    return longest


def _calendar_html(completed_days):
    month = calendar.Calendar(firstweekday=0)
    weeks = month.monthdayscalendar(MOCK_YEAR, MOCK_MONTH)
    month_name = date(MOCK_YEAR, MOCK_MONTH, 1).strftime("%B %Y")
    weekday_labels = "".join(
        f'<div class="weekday">{weekday}</div>'
        for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    )

    day_cells = []
    for week in weeks:
        for day_number in week:
            if day_number == 0:
                day_cells.append('<div class="day-cell empty"></div>')
                continue

            classes = ["day-cell"]
            if day_number in completed_days:
                classes.append("completed")
            if day_number in {4, 11, 18, 25}:
                classes.append("boss-day")

            label = "Completed" if day_number in completed_days else "Rest day"
            day_cells.append(
                f"""
                <div class="{' '.join(classes)}">
                    <span>{day_number}</span>
                    <small>{label}</small>
                </div>
                """
            )

    return f"""
        <article class="calendar-card">
            <div class="calendar-head">
                <div>
                    <div class="eyebrow">Training Codex</div>
                    <h2>{month_name}</h2>
                </div>
                <div class="calendar-badge">{len(completed_days)} clears</div>
            </div>
            <div class="calendar-grid weekdays">{weekday_labels}</div>
            <div class="calendar-grid">{''.join(day_cells)}</div>
        </article>
    """


def _inject_progress_css():
    render_html(
        """
        <style>
            :root {
                --spire-purple: #7C3AED;
                --spire-dark: #1A1A1A;
                --spire-light: #E5E5E5;
                --spire-panel: #232129;
                --spire-border: rgba(229, 229, 229, 0.13);
                --spire-muted: rgba(229, 229, 229, 0.66);
            }

            .stApp {
                background:
                    radial-gradient(circle at 10% 0%, rgba(124, 58, 237, 0.25), transparent 30rem),
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

            .progress-shell {
                color: var(--spire-light);
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            .progress-hero {
                border: 1px solid rgba(124, 58, 237, 0.4);
                border-radius: 8px;
                padding: 1.5rem;
                background:
                    linear-gradient(110deg, rgba(26, 26, 26, 0.96), rgba(35, 33, 41, 0.9)),
                    url("https://images.unsplash.com/photo-1514539079130-25950c84af65?auto=format&fit=crop&w=1600&q=80");
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

            .progress-hero h1,
            .calendar-head h2 {
                margin: 0.35rem 0 0;
                color: #FFFFFF;
                font-weight: 900;
                letter-spacing: 0;
            }

            .progress-hero h1 {
                max-width: 760px;
                font-size: clamp(2.1rem, 5vw, 4.2rem);
                line-height: 0.96;
            }

            .hero-copy {
                max-width: 720px;
                margin: 0.85rem 0 0;
                color: var(--spire-muted);
                font-size: 1.02rem;
                line-height: 1.6;
            }

            .metrics-grid {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 0.85rem;
                margin-top: 1rem;
            }

            .metric-card,
            .calendar-card,
            .reminder-card,
            .rune-card {
                border: 1px solid var(--spire-border);
                border-radius: 8px;
                background: linear-gradient(145deg, rgba(45, 41, 54, 0.96), rgba(26, 26, 26, 0.96));
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28);
            }

            .metric-card {
                padding: 1rem;
                min-height: 118px;
                border-top-color: rgba(124, 58, 237, 0.78);
            }

            .metric-label,
            .reminder-time {
                color: var(--spire-muted);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .metric-value {
                margin-top: 0.65rem;
                color: #FFFFFF;
                font-size: 2.2rem;
                font-weight: 900;
                line-height: 1;
            }

            .metric-note,
            .reminder-copy,
            .rune-copy {
                margin-top: 0.5rem;
                color: var(--spire-muted);
                line-height: 1.5;
            }

            .main-grid {
                display: grid;
                grid-template-columns: minmax(0, 1.35fr) minmax(300px, 0.8fr);
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

            .calendar-card {
                padding: 1rem;
            }

            .calendar-head {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                gap: 1rem;
                margin-bottom: 1rem;
            }

            .calendar-badge,
            .status-pill {
                border: 1px solid rgba(124, 58, 237, 0.52);
                border-radius: 999px;
                padding: 0.25rem 0.7rem;
                background: rgba(124, 58, 237, 0.16);
                color: #D8C8FF;
                font-size: 0.78rem;
                font-weight: 800;
                white-space: nowrap;
            }

            .calendar-grid {
                display: grid;
                grid-template-columns: repeat(7, minmax(0, 1fr));
                gap: 0.5rem;
            }

            .weekdays {
                margin-bottom: 0.5rem;
            }

            .weekday {
                color: rgba(229, 229, 229, 0.58);
                font-size: 0.75rem;
                font-weight: 850;
                text-align: center;
                text-transform: uppercase;
            }

            .day-cell {
                min-height: 82px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 0.65rem;
                border: 1px solid rgba(229, 229, 229, 0.1);
                border-radius: 8px;
                background: rgba(229, 229, 229, 0.055);
            }

            .day-cell span {
                color: #FFFFFF;
                font-size: 1rem;
                font-weight: 850;
            }

            .day-cell small {
                color: rgba(229, 229, 229, 0.52);
                font-size: 0.72rem;
                font-weight: 700;
            }

            .day-cell.completed {
                border-color: rgba(124, 58, 237, 0.65);
                background: linear-gradient(145deg, rgba(124, 58, 237, 0.46), rgba(45, 41, 54, 0.72));
                box-shadow: inset 0 0 22px rgba(124, 58, 237, 0.28);
            }

            .day-cell.boss-day:not(.completed) {
                border-color: rgba(229, 229, 229, 0.22);
            }

            .day-cell.empty {
                border-color: transparent;
                background: transparent;
                box-shadow: none;
            }

            .reminder-stack {
                display: grid;
                gap: 0.8rem;
            }

            .reminder-card,
            .rune-card {
                padding: 1rem;
            }

            .reminder-title,
            .rune-title {
                margin-top: 0.35rem;
                color: #FFFFFF;
                font-size: 1.05rem;
                font-weight: 850;
            }

            .completion-track {
                width: 100%;
                height: 18px;
                overflow: hidden;
                margin-top: 1rem;
                border: 1px solid rgba(229, 229, 229, 0.16);
                border-radius: 999px;
                background: rgba(229, 229, 229, 0.08);
            }

            .completion-fill {
                height: 100%;
                border-radius: 999px;
                background: linear-gradient(90deg, #7C3AED, #B58CFF);
                box-shadow: 0 0 28px rgba(124, 58, 237, 0.66);
            }

            .rune-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 1rem;
            }

            @media (max-width: 900px) {
                .metrics-grid,
                .main-grid {
                    grid-template-columns: 1fr;
                }

                .calendar-grid {
                    gap: 0.35rem;
                }

                .day-cell {
                    min-height: 64px;
                    padding: 0.45rem;
                }
            }
        </style>
        """,
    )


def show_progress():
    _inject_progress_css()

    total_days = calendar.monthrange(MOCK_YEAR, MOCK_MONTH)[1]
    completion_percentage = round((len(COMPLETED_DAYS) / total_days) * 100)
    completed_dates = {
        date(MOCK_YEAR, MOCK_MONTH, day_number) for day_number in COMPLETED_DAYS
    }
    current_streak = _current_streak(completed_dates)
    longest_streak = _longest_streak(completed_dates)

    reminder_cards = "".join(
        f"""
        <article class="reminder-card">
            <div class="reminder-time">{reminder["time"]}</div>
            <div class="reminder-title">{reminder["title"]}</div>
            <div class="reminder-copy">{reminder["copy"]}</div>
        </article>
        """
        for reminder in REMINDERS
    )

    render_html(
        f"""
        <main class="progress-shell">
            <section class="progress-hero">
                <div class="eyebrow">SPIRE Progress // Chronicle View</div>
                <h1>Track the rituals that strengthen your run.</h1>
                <p class="hero-copy">
                    Every completed exercise day lights another rune on the calendar.
                    Keep the chain alive, watch your completion climb, and prepare for
                    the next weekly reset.
                </p>
            </section>

            <section class="metrics-grid" aria-label="Progress statistics">
                <article class="metric-card">
                    <div class="metric-label">Current Streak</div>
                    <div class="metric-value">{current_streak}</div>
                    <div class="metric-note">Consecutive clears</div>
                </article>
                <article class="metric-card">
                    <div class="metric-label">Completion</div>
                    <div class="metric-value">{completion_percentage}%</div>
                    <div class="metric-note">{len(COMPLETED_DAYS)} of {total_days} days completed</div>
                </article>
                <article class="metric-card">
                    <div class="metric-label">Longest Streak</div>
                    <div class="metric-value">{longest_streak}</div>
                    <div class="metric-note">Best chain this month</div>
                </article>
                <article class="metric-card">
                    <div class="metric-label">Quest Days</div>
                    <div class="metric-value">{len(COMPLETED_DAYS)}</div>
                    <div class="metric-note">Exercise rituals logged</div>
                </article>
            </section>

            <section class="main-grid">
                <div>
                    <div class="section-title">Monthly Calendar</div>
                    {_calendar_html(COMPLETED_DAYS)}
                </div>

                <aside>
                    <div class="section-title">Streak Ward</div>
                    <article class="rune-card">
                        <div class="rune-row">
                            <div>
                                <div class="eyebrow">Monthly Completion</div>
                                <div class="rune-title">{completion_percentage}% of the ward restored</div>
                            </div>
                            <div class="status-pill">Active</div>
                        </div>
                        <div class="completion-track">
                            <div class="completion-fill" style="width: {completion_percentage}%"></div>
                        </div>
                        <div class="rune-copy">
                            Complete four more exercise days to unlock the next milestone reward.
                        </div>
                    </article>

                    <div class="section-title">Reminders</div>
                    <div class="reminder-stack">
                        {reminder_cards}
                    </div>
                </aside>
            </section>
        </main>
        """,
    )


show_progress()
