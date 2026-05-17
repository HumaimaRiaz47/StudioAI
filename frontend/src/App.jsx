import { useState } from "react";

import LandingPage from "./components/LandingPage";
import Dashboard from "./components/Dashboard";

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