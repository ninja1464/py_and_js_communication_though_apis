const express = require("express");
const axios = require("axios");
const app = express();
const port = 3001;

app.get("/callpython", async (req, res) => {
  const { a, b } = req.query; // Extract parameters from query

  if (!a || !b) {
    return res
      .status(400)
      .send("Missing required query parameters 'a' and 'b'");
  }

  try {
    // Log the parameters being sent
    console.log(`Making a call with parameters: a=${a}, b=${b}`);

    // Make a GET request to the external URL with dynamic parameters
    const response = await axios.get(
      `http://localhost:3000/data?a=${a}&b=${b}`
    );

    // Log the data received from the external URL
    console.log("Data received from Python server:", response.data);

    // Render a simple HTML response with the result
    res.send(`
      <html>
        <body>
          <h1>Result:</h1>
          <p>${response.data}</p>
        </body>
      </html>
    `);
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).send("Error fetching data");
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
