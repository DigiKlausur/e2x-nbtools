define(['base/js/namespace'], function(Jupyter) {

    let Notebook = Jupyter.Notebook;

    let old_add_checkpoint = Notebook.prototype.add_checkpoint;

    Notebook.prototype.add_checkpoint = function () {
        old_add_checkpoint.apply(this, arguments);
        this.list_checkpoints();
    }

});
