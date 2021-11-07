const express = require("express");
const cors = require("cors");
const config = require("./app/config");
const setupQuestionRoutes = require("./app/routes/question.routes");
const setupTestRoutes = require("./app/routes/test.routes");
const setupAuthRoutes = require("./app/routes/auth.routes");
const { BadRequestError } = require("./app/helpers/errors");
const db = require("./app/models");

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

MONGODB_URL = config.db.url;
db.mongoose
    .connect(MONGODB_URL)
    .then(() => {
        console.log("Ket noi co so du lieu thanh cong!");
    })
    .catch((error) => {
        console.log("Khong the ket noi co so du lieu!", error);
        process.exit();
    });

// simple route
app.get("/", (req, res) => {
    res.json({ message: "Dich vu API cho Anh Ngu Simple" });
});

setupQuestionRoutes(app);
setupTestRoutes(app);
setupAuthRoutes(app);

// handle 404 response
app.use((req, res, next) => {
    next(new BadRequestError(404, "Resource not found"));
});

// define error-handling middleware last, after other app.use() and routes calls
app.use((err, req, res, next) => {
    console.log(err);
    res.status(err.statusCode || 500).json({
        message: err.message || "Internal Server Error",
    });
});

// set port, listen for requests
const PORT = config.app.port;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});
