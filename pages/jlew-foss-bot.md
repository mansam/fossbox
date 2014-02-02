Title: Foss Bot
Url: /projects/foss-bot

[IRC Logs](/foss_bot/logs)

[Meeting Logs](/foss_bot/meetings)

# MeetBot

Foss bot runs the [MeetBot](http://wiki.debian.org/MeetBot) plugin.

## Common Commands

All commands are case-insensitive, and use the **#**prefix

#startmeeting

    Starts a meeting. The calling nick becomes the chair. If any text is given on the rest of the line, this becomes the meeting topic.
#endmeeting

    End a meeting, save logs, restore previous topic, give links to logs. You know the drill. (Chairs only.)
#topic

    Set the current topic of discussion. MeetBot changes the topic in the channel (saving the original topic to be restored at the end of  
the meeting). (Chairs only.)

#agreed (alias #agree)

    Mark something as agreed on. The rest of the line is the details. (Chairs only.)
#chair and #unchair

    Add new chairs to the meeting. The rest of the line is a list of nicks, separated by commas and/or spaces. The nick which started the meeting is the owner and can't be de-chaired. The command replies with a list of the current chairs, for verification (Chairs only.) Example:

