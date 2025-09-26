# Kuch Plan Hai - Frontend

A modern React frontend application for the "Kuch Plan Hai" project, featuring user authentication and a clean, responsive UI built with Vite and Tailwind CSS.

## Features

- 🔐 User Authentication (Login & Sign Up)
- 🎨 Modern UI with Tailwind CSS
- ⚡ Fast development with Vite
- 🧭 React Router for navigation
- 📱 Responsive design
- 🔧 ESLint for code quality

## Tech Stack

- **React 19** - Frontend framework
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router DOM** - Client-side routing
- **Heroicons** - Beautiful SVG icons
- **ESLint** - Code linting

## Getting Started

### Prerequisites

- Node.js (version 16 or higher)
- npm or yarn

### Installation

1. Clone the repository
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Create a `.env` file in the frontend directory and add:
   ```
   VITE_API_URL=http://localhost:8000
   ```

### Development

Start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
frontend/
├── public/          # Static assets
├── src/
│   ├── assets/      # Images and SVGs
│   ├── Login.jsx    # Login component
│   ├── SignUp.jsx   # Sign up component
│   ├── App.jsx      # Main app component
│   └── main.jsx     # Entry point
├── package.json
└── tailwind.config.js
```

## Backend Integration

This frontend connects to a FastAPI backend. Make sure your backend is running on the configured API URL (default: `http://localhost:8000`).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `npm run lint` to check for issues
5. Submit a pull request
