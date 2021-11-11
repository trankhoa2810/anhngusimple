module.exports = mongoose => {
    const schema = mongoose.Schema(
        {
            name: {
                type: String,
                required: [true, "Can nhap ten bai test"],
            },
            time:{
                type: Number,
                required: [true, "Can nhap thoi gian bai test"],
            },
            password:{
                type: String,
                required: [true, "Can nhap mat khau bai test"],
            },
            visible:{
                type: Boolean,
                required: [true, "Can chon trang thai bai test"],
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

    return mongoose.model("test", schema);
};
