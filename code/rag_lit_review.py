## References:
# https://python.langchain.com/docs/tutorials/rag/
# https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html
# https://python.langchain.com/docs/concepts/vectorstores/
# https://python.langchain.com/api_reference/ollama/llms/langchain_ollama.llms.OllamaLLM.html
# https://python.langchain.com/api_reference/huggingface/embeddings/langchain_huggingface.embeddings.huggingface.HuggingFaceEmbeddings.html
# used gpt for debugging and suggestions

## BEFORE RUNNING: Have ollama installed locally, run "ollama serve" in another terminal

## import libraries and modules
import json
import pathlib
import re
import pymupdf4llm
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_huggingface import HuggingFaceEmbeddings


## declare global variables

# paper filepaths
file_path_list = ["ahmetovic21.pdf", "ahsen22.pdf", "alankus11.pdf", "allen23.pdf", "allmen09.pdf", "alsaleem19.pdf",
"alves21.pdf", "anderson96.pdf", "andradi21.pdf", "anthony12.pdf", "aruanno18.pdf", "asakawa21.pdf", "aziz08.pdf", 
"baloian02.pdf", "balter05.pdf", "bandukdta20.pdf", "barbeschi20.pdf", "barbeschi22.pdf", "barbel18.pdf", "batterman13.pdf",
"bennett19.pdf", "bhatt20.pdf", "biemanns09.pdf", "bircanin20.pdf", "black11.pdf", "bondioli17.pdf", "boyd23.pdf", "boyd17.pdf",
"breashear06.pdf", "brule16.pdf", "bushmann14.pdf", "butler19.pdf", "butler23.pdf", "capozzi12.pdf", "caro14.pdf", "carrington17.pdf",
"carrington18.pdf", "cavasosquero18.pdf", "chang16.pdf", "chibaudel20.pdf", "cimolino21.pdf", "collins23.pdf", "conde20.pdf",
"constantin18.pdf", "desilva23.pdf", "dragomir18.pdf", "duval18.pdf", "fan12.pdf", "fell03.pdf", "folmer09.pdf", "franz23.pdf",
"friedman18.pdf", "fung22.pdf", "gadiraju19.pdf", "gadiraju21.pdf", "galbraith14.pdf", "galliers11.pdf", "gay20.pdf", "gelsomini16.pdf",
"gennari08.pdf", "gerling13.pdf", "gizatdinova22.pdf", "gleason20.pdf", "gonclaves20.pdf", "gotfrid16.pdf", "hair19.pdf", "hamidi17.pdf",
"harada07.pdf", "hine02.pdf", "hiraga06.pdf", "hoey10.pdf", "hoffman15.pdf", "hornof03.pdf", "hossain23.pdf", "hurd19.pdf", "husaan11.pdf",
"illijima22.pdf", "ilsar20.pdf", "india21.pdf", "india19.pdf", "jack00.pdf", "jain19.pdf", "jayant11.pdf", "jiang23.pdf", "jiang22.pdf", "kamel02.pdf",
"kamel00.pdf", "kaminer14.pdf", "karpodini22.pdf", "keate94.pdf", "khurana21.pdf", "kim11.pdf", "kim13.pdf", "koseff23.pdf", "koushik17.pdf",
"kurze96.pdf", "kuwahara06.pdf", "kwon19.pdf", "langford21.pdf", "lehman98.pdf", "franz21.pdf", "li22.pdf", "li22_2.pdf", "lobo21.pdf",
"lobo19.pdf", "lu22.pdf", "lu23.pdf", "luna23.pdf", "macpherson18.pdf", "madeo11.pdf", "madjaroff17.pdf", "mahmud23.pdf", "mahmud06.pdf", "maidenbaum15.pdf",
"mai22.pdf", "malik21.pdf", "mandryk12.pdf", "martinez21.pdf", "mascetti19.pdf", "mcgowan23.pdf", "mcgowan17.pdf", "mei15.pdf", "menzies19.pdf",
"miao17.pdf", "miller07.pdf", "milne13.pdf", "milne14.pdf", "mohammed06.pdf", "mok22.pdf", "mok23.pdf", "montague14.pdf", "moore03.pdf",
"morales16.pdf", "morelli10.pdf", "morris10.pdf", "mott20.pdf", "moyaalcover11.pdf", "myers02.pdf", "nair22.pdf", "norte08.pdf", "obryan12.pdf",
"ohshiro22.pdf", "omori13.pdf", "oren08.pdf", "ortega15.pdf", "ostiz-blanco18.pdf", "ostiz-blanco18-2.pdf", "pareto05.pdf", "parnandi13.pdf",
"payne22.pdf", "payne23.pdf", "payne20.pdf", "payne19.pdf", "piedade23.pdf", "piper10.pdf", "pires19.pdf", "plaisant00.pdf", "poddar23.pdf",
"porter13.pdf", "putnam13.pdf", "putnam08.pdf", "ragone20.pdf", "raman98.pdf", "rauschenberger15.pdf", "ravers23.pdf", "rector13.pdf", "rello15.pdf",
"rello12.pdf", "rello14.pdf", "rello17.pdf", "ringland19.pdf", "ridngland16.pdf", "rocha 21.pdf", "rubin16.pdf", "saha17.pdf", "sanchez11.pdf", "sanchez03.pdf",
"sanchez05.pdf", "sanchez09.pdf", "sanchez10.pdf", "seymour17.pdf", "sharma18.pdf", "shamra16.pdf", "shin20.pdf", "smeddink15.pdf", "smeddink13.pdf",
"sporka13.pdf", "sporka06.pdf", "stangl15.pdf", "sturm17.pdf", "swaminathan18.pdf", "tamburro20.pdf", "torrente12.pdf", "torrente12-2.pdf", "trewin18.pdf",
"trinh11.pdf", "tzanidou22.pdf", "tzovaras02.pdf", "uchida17.pdf", "uchida18.pdf", "usui10.pdf", "valencia19.pdf", "vuijk21.pdf", "wilkerson10.pdf", "wilson17.pdf",
"yairi12.pdf", "ye12.pdf", "yuan08.pdf", "zhang22.pdf", "zhang23.pdf", "zhang23-2.pdf"]


# single paper filepath to use in testing, comment out if not using
#file_path_list = ["ahmetovic21.pdf"]

# metrics list
pht_framework = [
    "What is the DOI for this paper?",

    "What is the title of the paper?",

    "Who is the lead author of the paper?",

    "What year was this paper published?",

    "How many pages long is this paper?",

    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) totally fun first (i.e., Entertainment game reappropriated), 
    (2) mostly fun first (i.e., design workshop with disabled stakeholders),
    (3) both fun and utility first (i.e., design workshop with diverse stakeholders), 
    (4) mostly utility first (i.e., primary utilitarian mechanic designed first),
    (5) totally utility first (i.e., made by clinicians or specialists, fun incorporated later)""",
    
    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) unstructured play (i.e., no rules, making art),
    (2) semi-structured play (i.e., playground activities),
    (3) flexible structure with rules (i.e., improv),
    (4) flexible game (i.e., board game with house rules),
    (5) game with rigid rules (i.e., video game)""",
    
    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) entirely skill-based (i.e., trivia, sports),
    (2) mostly skill-based (i.e., mario kart),
    (3) equally skill and chance-based (i.e., catan),
    (4) mostly chance-based (i.e., Uno),
    (5) entirely chance-based (i.e., all dice)""",
    
    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) entirely solo (i.e., solitaire),
    (2) mostly solo (i.e., playing against AI in single-player StarCraft),
    (3) mix of solo and social affordances (i.e., animal crossing),
    (4) mostly social, but aspects are independent (i.e., house on hill haunt transition),
    (5) entirely social (i.e., tag)""", 
    
    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) entirely turn-based (i.e., tic tac toe),
    (2) follows a set of steps (i.e., viticulture's dynamic turn ordering),
    (3) turns are taken, but some actions can be taken at any time (i.e., pandemic),
    (4) most actions can be taken at any time, but there are some phases (i.e., PvP death reset timer),
    (5) entirely simultaneous (i.e., race)""",
    
    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) entirely synchronous (i.e., real time strategy game),
    (2) mostly synchronous with a few asynchronous affordances (i.e., league of legends),
    (3) equal mix of synchronous and asynchronous affordances (i.e., helldivers 2),
    (4) mostly asynchronous with few synchronous affordances (i.e. cookie clicker),
    (5) entirely asynchronous (i.e., chess by postage mail)""",

    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) entirely competitive (i.e., spit card game),
    (2) mostly competitive, but sometimes collaboration is important (i.e., forbidden island),
    (3) mix of competitive and collaborative (i.e., mario party 2 vs 2 mini-games),
    (4) mostly collaborative (i.e., animal crossing),
    (5) entirely collaborative (i.e., pandemic)""",

    """Please answer this question with a number--which of the following best apply to the design in the study: 
    (1) entirely symmetrical (i.e., tic tac toe),
    (2) mostly symmetrical (i.e., undertale's differing NPC behaviors based on previous playthroughs),
    (3) both symmetrical and asymmetrical (i.e., pandemic with its similar turn structure but different character abilities),
    (4) mostly asymmetrical (i.e., tag),
    (5) entirely asymmetrical (i.e., keep talking, nobody explodes)""",
    
    """How would you classify the experiential play value? Do not add additional context or reasoning in your response: 
    sensority (i.e. kaleidoscope, experiencing art), 
    fantasy (i.e. role-playing), 
    construction (i.e. music, painting, building), 
    challenge (testing physical or mental abilities against others or self), 
    undisclosed/unknown, but the paper does include a game/play system or experience, 
    not applicable""",

    """Which of the following study methods applies to this paper? Please select all that apply:
    workshop or design session, 
    field study, 
    usability testing, 
    case study, 
    focus group,
    controlled experiment, 
    survey, 
    telemetry/big data/cscw, 
    secondary analysis, 
    no data collected,
    other (please specify)""",

    """Which of the following interview methodologies was used? Select all that apply: 
    structured interview,
    semi-structured interview, 
    contextual inquiry, 
    not applicable, 
    other (please specifcy)""",

    """Which of the following workshop methodologies were used? Select all that apply:
     action research, cooperative method development, speculative design, persona, scenario, role playing, 
     affinity diagram, ideation, user journey, brainstorming, bodystorming, design probe, prototyping, mock-up,
     sketching, wireframing, card sotring, storyboarding, use case theater, object theater, not applicable,
     other (please specify)""",

     """Which of the following field study methodologies where used? Please select all that apply: autoethnography,
     ethnography, diary study, cultural, Wizard of Oz, not applicable, other (please specify)""",

     """Which of the following usability methodologies were used? Please select all that apply: expert analysis, think 
     aloud, cognative walkthrough, heuristic analysis, not applicable, other (please specify)""",

     """Which of the following technology modalities were used? Please select all that apply: mobile, tablet, wearable, IoT, 
     assistive devices, robot, tangible interface, PC, virtual reality, augmented reality, game console, no technology, other (please specify)""",

     """What was the context of the study? Please select all that apply: clinic, public space (i.e. bowling alley), home, school, research lab, 
     social media, disability community space (i.e. Day program), remote/Zoom, not applicable, other (please specify)""",

     """What was the community of focus? Please select all that apply: Blind or low vision (BLV), Deaf or hard of hearing (DHH), Autism, 
     intellectual or developmental disability (IDD), motor of physical impairment, communication/speech, cognitive impairment, older adult, 
     general disability or accessability, other (please specifiy)""",

    """What were the participant groups included in the study? Please select all that apply: People with disabilities, older adults, caregivers, 
    specialists (e.g. therapists, teachers), people without disabilities, no user involvement, other (please specify)""",

    """Please select the option(s) that best describe user involevment in the study: participatory design with stakeholders without disabilities, 
    participatory design with stakeholders with disabilities, user evaluation with stakeholders without disabilities, user evaluation with stakeholders 
    with disabilities, no representative user involvement, not applicable""",

    """Which methods of participant recruitment were used? Please select all that apply: phone, mail, email, convienience sampling (i.e. Day program), 
    snowball, word of mouth, flier, social media, clinic, no user involvement, undisclosed, other (please specify)""",

    """Which of the following issues were addressed in the study? Please select all that apply: increasing independence, increasing digital access, 
    increasing physical access, increasing understanding of users, supporting communication, personal informatics and changing behavior,
    education, increasing opportunities for enrichment, other""",

    """What is the type of contribution the study makes? Please select all that apply: empirical, artifact, methodological, theoretical, dataset, survey"""
]

# set up llm
llm = Ollama(model="llama2", temperature=0.5)
# ref for model: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

### functions ###

# name: load_pdf
# input: file path
# return: markdown object
# description: loads in pdf, converts to markdown
def load_pdf(file_path):
    ## convert file to markdown format so it can be chunked
    markdown_text = pymupdf4llm.to_markdown(file_path)
    ## write to a file using UTF-8 encoding
    pathlib.Path("output.md").write_bytes(markdown_text.encode())
    chunked_data = chunk_data(markdown_text)
    return chunked_data

# name: chunk_data
# input: markdown text
# return: chunked data of type TYPE
# description: chunks text for further processing
def chunk_data(text):
    split_text = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    chunked_doc = split_text.create_documents([text])
    return chunked_doc

# name: create_vec
# input: chunked_data
# return: vector_store
# description: places chunked data into a vector store
def create_vec(chunked_data):
    vector_store = InMemoryVectorStore(embedding=embedding_model)
    vector_store.add_documents(documents=chunked_data)
    return vector_store

# name: prompt
# input: vector_store
# return: list of annotations
# description: prompts the model to apply annotations
def prompt(vector_store, paperID):
    # list of annotations
    annotations = []
    # for each metric
    for metric in pht_framework:
        # retrieve context using vector_store
        context = retrieve(vector_store, metric)

        # full prompt
        # needs work
        full_prompt = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer. Do not repeat the question in your response.
 
        Return your answer in the following format:
        Answer: <only the answer here>
        Reasoning: <any explaination or reasoning goes here>

        {context}

        Question: {metric}

        """

        # generate response using llm
        response = generate(context, metric, full_prompt, paperID)
        annotations.append(response)
    return annotations


# name: retrieve
# input: vector_store, metric
# return: context
# description: uses metric and vector_store to gather context for prompting
def retrieve(vector_store, metric):
    retrieved_context = vector_store.similarity_search(metric)
    return retrieved_context

# name: generate
# input: context, metric
# return: annotation
# description: uses context and metric to apply annotation
def generate(context, metric, full_prompt, paperID):
    docs_content = "\n\n".join(doc.page_content for doc in context)
    prompt_text = full_prompt.format(context = docs_content, metric = metric)
    response = llm(prompt_text).strip()

    answer_match = re.search(r"(?i)^Answer:\s*(.*)", response, re.MULTILINE)
    reasoning_match = re.search(r"(?i)^Reasoning:\s*(.*)", response, re.MULTILINE)

    answer = answer_match.group(1).strip() if answer_match else "Not found"
    reasoning = reasoning_match.group(1).strip() if reasoning_match else "Not found"

    return {
        "paperID": paperID,
        "question": metric,
        "answer": answer,
        "reasoning": reasoning
        }

# name: generate_json
# input: annotation_list
# return: json output
# description: creates json file based on annotations
def generate_json(annotation_list, file_num):
    output_path= f"outputs/annotations_{file_num}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(annotation_list, f, indent=2, ensure_ascii=False)

## main function
def main():
    # load file path (will set up to iterate over list of file paths later)
    file_num = 1
    for file in file_path_list:
        file_path = f"../papers/{file}"
        # break data into chunks
        chunked_data = load_pdf(file_path)
        # store chunks in vector
        vector_store = create_vec(chunked_data)
        # apply annotations to paper
        annotations = prompt(vector_store, file_num)
        # generate json file containing annotations for that specific paper
        generate_json(annotations, file_num)
        file_num = file_num + 1
        print("Complete.")

if __name__ == "__main__":
    main()