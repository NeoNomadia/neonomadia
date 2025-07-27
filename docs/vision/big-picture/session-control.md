# Session Control

The **NeoNomadia** project allows usage in anonymous mode via any compliant frontend. Users retain full autonomy over how long their interaction data is stored. By default, all session data must be deleted 15 minutes after the last session refresh. Even authenticated users may define their own data retention interval, including the option to have all interaction data forgotten.

It is the responsibility of the frontend to clearly inform users about session expiration and their available choices:

- **Forget all after session**
- **Keep session to be continued** — either indefinitely, with a defined expiration interval (e.g., "2 hours," "7 days"), or a fixed expiration date (e.g., "2025-08-01")
- **Pause session** — signaling that the user has intentionally paused activity, with no refresh expected within the next 15 minutes

The `get_session` interface accepts an optional `session_id` parameter (e.g., via a session cookie) to resume an existing session. If the session is authenticated but the authentication has expired, re-authentication is required.

All session-related functions must adhere to the principle of **maximum information sovereignty**.

To uphold this principle, the open API is restricted to **registered consumers only**. Unregistered consumers are not permitted to initiate sessions. This ensures that every consumer complies with the core cooperation standards and the NeoNomadia code of conduct, aligned with the project’s ethical goals.
