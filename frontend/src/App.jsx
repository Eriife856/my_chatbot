import React from "react";
import Headers from "./Headers";
import ChatBots from "./ChatBots";
import "./App.css"

const App = () => {
  return (
    <div className="min-h-screen bg-gray-200">
      <Headers />
      <ChatBots />
    </div>
  );
};

export default App;
