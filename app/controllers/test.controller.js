const { BadRequestError } = require("../helpers/errors");
const handle = require("../helpers/promise");
const db = require("../models");
const Test = db.Test;

exports.create = async (req, res, next) => {
    if (!req.body.name || !req.body.time || !req.body.password) {
        return next(new BadRequestError(400, "Thong tin de bai bi thieu"));
    }
    const test = new Test({
        name: req.body.name,
        time: req.body.time,
        password: req.body.password,
        visible: req.body.visible,
        ownerId: req.userId,
    });
    const [error, document] = await handle(test.save());
    if (error) {
        return next(
            new BadRequestError(
                500,
                "Loi trong qua trinh tao de bai"
            )
        );
    }

    return res.send(document);
};

exports.findAll = async (req, res, next) => {
    const [error, documents] = await handle(
        Test.find({}, "-ownerId")
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                "Loi truy xuat de bai"
            )
        );
    }
    return res.send(documents);
};

exports.findOne = async (req, res, next) => {
    const condition = {
        _id: req.params.id,
        ownerId: req.userId,
    };
    const [error, document] = await handle(
        Test.findOne(condition, "-ownerId")
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                `Loi truy xuat de bai id=${req.params.id}`
            )
        );
    }
    if (!document) {
        return next(new BadRequestError(404, "De bai khong ton tai"));
    }
    return res.send(document);
};

exports.update = async (req, res, next) => {
    if (!req.body) {
        return next(
            new BadRequestError(400, "Thong tin cap nhat de bai bi thieu")
        );
    }
    const condition = {
        _id: req.params.id,
        ownerId: req.userId,
    };
    const [error, document] = await handle(
        Test.findOneAndUpdate(condition, req.body, {
            new: true,
            projection: "-ownerId",
        })
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                `Loi cap nhat de bai id=${req.params.id}`
            )
        );
    }
    if (!document) {
        return next(new BadRequestError(404, "De bai khong ton tai"));
    }

    return res.send({ message: "Cap nhat de bai thanh cong" });
};

exports.delete = async (req, res, next) => {
    const condition = {
        _id: req.params.id,
        ownerId: req.userId,
    };
    const [error, document] = await handle(
        Test.findOneAndDelete(condition, {
            projection: "-ownerId",
        })
    );
    if (error) {
        return next(
            new BadRequestError(
                500,
                `Khong the xoa de bai id=${req.params.id}`
            )
        );
    }
    if (!document) {
        return next(new BadRequestError(404, "De bai khong ton tai"));
    }
    return res.send({ message: "Xoa de bai thanh cong" });
};
