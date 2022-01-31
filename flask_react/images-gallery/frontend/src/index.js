import React from "react";
import ReactDOM from "react-dom";
import "./css/index.css";
import App from "./App";

const a = false;

ReactDOM.render(
  <React.StrictMode>{a ? <App /> : <h1>Hola from JSX!</h1>}</React.StrictMode>,
  document.getElementById("root")
);
