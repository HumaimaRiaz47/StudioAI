import { useState } from 'react'
import LandingPage from './Pages/LandingPage.jsx'
import Dashboard from './Pages/Dashboard.jsx'

export default function StudioAIApp() {
  const [started, setStarted] = useState(false)

  if (started) {
    return <Dashboard />
  }

  return <LandingPage onStart={() => setStarted(true)} />
}