import { useState } from "react";

import LandingPage from "./pages/LandingPage.jsx";
import Dashboard from "./Pages/Dashboard.jsx";

export default function App() {
  const [started, setStarted] = useState(false);

  if (started) {
    return <Dashboard />;
  }

  return (
    <LandingPage
      onStart={() => setStarted(true)}
    />
  );
}