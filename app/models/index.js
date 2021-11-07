const mongoose = require("mongoose");
const createQuestionModel = require("./question.model");
const createTestModel = require("./test.model");
const createUserModel = require("./user.model");

const db = {};
db.mongoose = mongoose;
db.Question = createQuestionModel(mongoose);
db.Test = createTestModel(mongoose);
db.User = createUserModel(mongoose);

module.exports = db;