const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.use(express.static('public')); // Serve static files from the "public" directory

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
