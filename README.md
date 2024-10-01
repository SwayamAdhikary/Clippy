# Clipboard Sync App

This project is a simple **clipboard-sharing app** built using **Flask** and **WebSockets**. It allows users to sync copied text between multiple devices in real-time. The app features session management so users can join a shared clipboard session using a topic name. Without the topic name, the clipboard cannot be accessed, ensuring session privacy.

## Features

- **Real-Time Syncing**: Text copied on one device is instantly available on another device.
- **Session Management**: Users must provide a session topic name to access the shared clipboard. This ensures only authorized users can join the session.
- **Cross-Device Support**: Works seamlessly across different devices (e.g., phones, laptops).
- **End Session**: Ability to terminate a session, preventing further clipboard access.
- **UI/UX**: A minimalistic, dark-themed interface with a central focus on the clipboard, featuring the app name **"ClipNow"**.

## Tech Stack

- **Backend**: Flask, WebSockets
- **Frontend**: HTML, CSS (dark purple theme)
- **Deployment**: Flask server locally or via cloud platforms

## How It Works

1. **Login**: Users can create or join a clipboard session by providing a session topic name.
2. **Clipboard Sync**: Any text pasted into the app is sent across all connected devices.
3. **Copy All**: A single button to copy the entire text from the clipboard.
4. **End Session**: Clicking the "End Session" button disconnects all users from the current session.

## Future Improvements

- **User Authentication**: Add login functionality to secure clipboard access.
- **Encryption**: Encrypt the data being shared across devices for added security.
- **File Sharing**: Extend clipboard functionality to support file sharing.


