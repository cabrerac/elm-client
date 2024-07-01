from transformers import pipeline

qa_model = pipeline("question-answering")


def interact(context):
    question = ""
    context = _format_context(context)
    while question != "end":
        question = input("Type your question... (Type 'end' to finish)")
        qa = qa_model(question=question, context=context)
        print(qa["answer"])


def _format_context(context):
    formatted_context = "This is the process that a learning model followed model a given dataset."
    for record in context:
        if record["finished"]:
            task = record["task"]
            formatted_context = formatted_context + " " + str(task)
    return formatted_context
