module.exports = mongoose => {
    const schema = mongoose.Schema(
        {
            content: {
                type: String,
                required: [true, "Can nhap noi dung cau hoi"],
            },
            a: {
                type: String,
                required: [true, "Can nhap noi dung cua dap an a"],
            },
            b: {
                type: String,
                required: [true, "Can nhap noi dung cua dap an b"],
            },
            c: {
                type: String,
                required: [true, "Can nhap noi dung cua dap an c"],
            },
            d: {
                type: String,
                required: [true, "Can nhap noi dung cua dap an d"],
            },
            answer: {
                type: String,
                required: [true, "Can nhap noi dung dap an"],
            },
            testId: {
                type: String,
                required: [true, "Can nhap id cua test"],
            },
            ownerId: {
                type: mongoose.Schema.Types.ObjectId,
                ref: "user"
            },
        },
        { timestamps: true }
    );

    // Replace _id with id and remove __V
    schema.method("toJSON", function () {
        const { __v, _id, ...object } = this.toObject();
        object.id = _id;
        return object;
    });

    return mongoose.model("question", schema);
};
