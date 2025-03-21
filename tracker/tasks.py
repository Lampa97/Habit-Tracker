from celery import shared_task
from django.utils import timezone

from .services import send_tg_message

@shared_task
def send_habit_notification(user, chat_id, habit):
    user_habits = user.habits.all()
    if habit in user_habits:
        last_scheduled = habit.last_scheduled or timezone.now()
        habit.last_scheduled = last_scheduled
        habit.save()
        next_schedule = last_scheduled + timezone.timedelta(days=habit.periodicity_in_days)
        additional_text = ""
        if habit.connected_habit:
            additional_text += f"First complete {habit.connected_habit.action} habit too! "
        if habit.is_pleasant:
            additional_text += "Don't forget to enjoy it! "
        if habit.reward:
            additional_text += f"Your reward will be {habit.reward}."

        text = f"""
        Hey, {user.email}! Don't forget to complete your habit at {habit.time}: {habit.action} at {habit.place}!
        You need {habit.time_to_finish} seconds to finish it.
        {additional_text}.
        Last scheduled: {last_scheduled}.
        Next schedule: {next_schedule}.
"""
        send_tg_message(text, chat_id)
