Postmortem
Issue Summary
On January 1, 2023, from 12:00 PM to 3:00 PM (EST), our main website was down, impacting 100% of our users. The root cause was an expired SSL certificate.

Timeline
12:00 PM: The issue was detected by a monitoring alert that checks the website's uptime.
12:10 PM: Initial investigation started, assuming it might be a server overload issue.
12:30 PM: The server load was found to be normal, ruling out the initial assumption.
1:00 PM: The issue was escalated to the network team.
2:00 PM: The network team identified the expired SSL certificate as the root cause.
3:00 PM: The SSL certificate was renewed and the website was back up.
Root Cause and Resolution
The issue was caused by an expired SSL certificate. The website's security protocol requires a valid SSL certificate for the website to be accessible. When the certificate expired, the website became inaccessible.

The issue was resolved by renewing the SSL certificate. The network team generated a new certificate and installed it on the server, which brought the website back online.

Corrective and Preventive Measures
To prevent this issue from happening again, we can:

Implement a system to track and alert for SSL certificate expiration dates.
Automate the SSL certificate renewal process to minimize human error.
Specific tasks to address the issue:

Implement an SSL certificate monitoring system that sends alerts 30 days before expiration.
Research and implement an automated SSL certificate renewal system.
This postmortem is a brief and straight-to-the-point document that outlines the issue, its cause, how it was resolved, and the steps we're taking to prevent it from happening again.

