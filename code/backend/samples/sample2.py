
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os


"""
FILE: sample_extract_summary.py

DESCRIPTION:
  This sample demonstrates how to submit text documents for extractive text summarization.
  Extractive summarization is available as an action type through the begin_analyze_actions API.

USAGE:
  python sample_extract_summary.py

  Set the environment variables with your own values before running the sample:
  1) AZURE_LANGUAGE_ENDPOINT - the endpoint to your Language resource.
  2) AZURE_LANGUAGE_KEY - your Language subscription key
"""


def sample_extractive_summarization(document):  
    print(document)
    # [START extract_summary]

    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
    key = os.getenv("AZURE_LANGUAGE_KEY")

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )


    # document = [
    #     "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, "
    #     "human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI Cognitive "
    #     "Services, I have been working with a team of amazing scientists and engineers to turn this quest into a "
    #     "reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of "
    #     "human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the "
    #     "intersection of all three, there's magic-what we call XYZ-code as illustrated in Figure 1-a joint "
    #     "representation to create more powerful AI that can speak, hear, see, and understand humans better. "
    #     "We believe XYZ-code will enable us to fulfill our long-term vision: cross-domain transfer learning, "
    #     "spanning modalities and languages. The goal is to have pretrained models that can jointly learn "
    #     "representations to support a broad range of downstream AI tasks, much in the way humans do today. "
    #     "Over the past five years, we have achieved human performance on benchmarks in conversational speech "
    #     "recognition, machine translation, conversational question answering, machine reading comprehension, "
    #     "and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious "
    #     "aspiration to produce a leap in AI capabilities, achieving multisensory and multilingual learning that "
    #     "is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational "
    #     "component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
    # ]

    poller = text_analytics_client.begin_extract_summary(document)
    extract_summary_results = poller.result()

    summary_text = ""

    for result in extract_summary_results:
        if result.kind == "ExtractiveSummarization":
            # print(
            #     "Summary extracted: \n{}".format(
            #         " ".join([sentence.text for sentence in result.sentences])
            #     )
            # )
            for sentence in result.sentences:
                summary_text += sentence.text + " "  # Add space after each sentence

        elif result.is_error is True:
            print(
                "...Is an error with code '{}' and message '{}'".format(
                    result.error.code, result.error.message
                )
            )
        # [END extract_summary]

        return summary_text