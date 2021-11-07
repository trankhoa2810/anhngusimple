const { BadRequestError } = require("../helpers/errors");
const handle = require("../helpers/promise");
const db = require("../models");
const Question = db.Question;

exports.create = async (req, res, next) => {
    if (!req.body.content || !req.body.a || !req.body.b || !req.body.c || !req.body.d || !req.body.answer || !req.body.testId) {
        return next(new BadRequestError(400, "Thong tin cau hoi bi thieu"));
    }
    const question = new Question({
        content: req.body.content,
        a: req.body.a,
        b: req.body.b,
        c: req.body.c,
        d: req.body.d,
        answer: req.body.answer,
        testId: req.body.testId,
        ownerId: req.userId,
    });
    const [error, document] = await handle(question.save());
    if (error) {
        return next(
            new BadRequestError(
                500,
                "Loi trong qua trinh them cau hoi"
            )
        );
    }

    return res.send(document);
};

exports.update = async (req, res, next) => {
    if (!req.body) {
        return next(
            new BadRequestError(400, "Thong tin cap nhat bi thieu")
        );
    }
    const condition = {
        _id: req.params.id,
        ownerId: req.userId,
    };
    const [error, document] = await handle(
        Question.findOneAndUpdate(condition, req.body, {
            new: true,
            projection: "-ownerId",
        })
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                `Loi cap nhat cau hoi id=${req.params.id}`
            )
        );
    }
    if (!document) {
        return next(new BadRequestError(404, "Cau hoi khong ton tai"));
    }
    return res.send({ message: "Cap nhat cau hoi thanh cong" });
};

exports.delete = async (req, res, next) => {
    const condition = {
        _id: req.params.id,
        ownerId: req.userId,
    };
    const [error, document] = await handle(
        Question.findOneAndDelete(condition, {
            projection: "-ownerId",
        })
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                `Khong the xoa cau hoi id=${req.params.id}`
            )
        );
    }
    if (!document) {
        return next(new BadRequestError(404, "Cau hoi khong ton tai"));
    }

    return res.send({ message: "Xoa cau hoi thanh cong" });
};

exports.findAll = async (req, res, next) => {
    const [error, documents] = await handle(
        Question.find(
            {
                testId: req.params.testId,
                ownerId: req.userId,
            },
            "-ownerId"
        )
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                `Loi trong qua trinh truy xuat du lieu cua testId=${req.params.testId}`
            )
        );
    }
    return res.send(documents);
};
