const express = require("express");
const question = require("../controllers/question.controller");
const middlewares = require("../middlewares");

module.exports = app => {
    const router = express.Router();

    router.use(middlewares.verifyToken);

    router.post("/", question.create);
    router.get("/:testId", question.findAll);
    router.put("/:id", question.update);
    router.delete("/:id", question.delete);

    app.use("/api/questions", router);
};
