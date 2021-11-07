const express = require("express");
const test = require("../controllers/test.controller");
const middlewares = require("../middlewares");

module.exports = app => {
    const router = express.Router();

    router.use(middlewares.verifyToken);

    router.post("/", test.create);
    router.get("/", test.findAll);
    router.get("/:id", test.findOne);
    router.put("/:id", test.update);
    router.delete("/:id", test.delete);

    app.use("/api/tests", router);
};
