import openai


# model="gpt-3.5-turbo"
# model="gpt-4"
model="gpt-4-turbo-preview"
# temperature = 1.0
# top_p = 1.0
# presence_penalty = 1.0
# temperature = 0.7
# top_p = 0.9
# presence_penalty = 0.5
temperature = 0.2
top_p = 0.5
presence_penalty = 0.0
prompt = "Give me the sentiment conveyed in this text: Positive, Negative, or Neutral - I had a bad experience at this restaurant, I asked for a spicy level 5 and it was bland. The service was too slow, the place was filthy"


response = openai.ChatCompletion.create(
  api_key="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",
  model=model,
  messages=[{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],
  temperature=temperature,  # Set the temperature
  max_tokens=1000,   # Limit the response length
  top_p=top_p,        # Apply top-p sampling
  frequency_penalty=0,  # No frequency penalty
  presence_penalty=presence_penalty  # Encourage introducing new topics
)

print("Model ==>", model, "\n",
  "Prompt ==>", prompt, "\n",
      "Response ==>", response["choices"][0]["message"]["content"], "\n",
      "Temperature ==>", temperature, "\n",
      "Top-p Sampling ==>", top_p, "\n",
      "Presence Penalty ==>", presence_penalty, "\n",
      "---------------------------------------------------------------------------------------------------------------------------------")

prompt = "Give me the sentiment conveyed in this text: Positive, Negative, or Neutral - “I am fine.” Sentiment – Neutral. “The weather is just right today, nothing too special or too extraordinary about it.” Sentiment – [Your Answer]"


response = openai.ChatCompletion.create(
  api_key="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",
  model=model,
  # model="gpt-4",
  # model="gpt-4-turbo-preview",
  messages=[{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],
  temperature=temperature,  # Set the temperature
  max_tokens=1000,   # Limit the response length
  top_p=top_p,        # Apply top-p sampling
  frequency_penalty=0,  # No frequency penalty
  presence_penalty=presence_penalty  # Encourage introducing new topics
)

print("Model ==>", model, "\n",
  "Prompt ==>", prompt, "\n",
      "Response ==>", response["choices"][0]["message"]["content"], "\n",
      "Temperature ==>", temperature, "\n",
      "Top-p Sampling ==>", top_p, "\n",
      "Presence Penalty ==>", presence_penalty, "\n",
      "---------------------------------------------------------------------------------------------------------------------------------")


prompt = "Give me the sentiment conveyed in this text: Positive, Negative, or Neutral - “My Big Data professor is so knowledgeable. She has an enormous set of projects and topics she specializes in, and her way of imparting knowledge is amazing too. The projects are well-though of too.” Sentiment – Positive. “Critics argue that recent improvements in the school system are merely superficial.” Sentiment – Negative. “The product arrived on time; it is in working condition, but the packaging was damaged in transit.” Sentiment – Neutral. “Educational technology has the potential to revolutionize learning, but it also poses risks.”. Sentiment – [Your Answer]"


response = openai.ChatCompletion.create(
  api_key="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",
  model=model,
  # model="gpt-4",
  # model="gpt-4-turbo-preview",
  messages=[{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],
  temperature=temperature,  # Set the temperature
  max_tokens=1000,   # Limit the response length
  top_p=top_p,        # Apply top-p sampling
  frequency_penalty=0,  # No frequency penalty
  presence_penalty=presence_penalty  # Encourage introducing new topics
)

print("Model ==>", model, "\n",
  "Prompt ==>", prompt, "\n",
      "Response ==>", response["choices"][0]["message"]["content"], "\n",
      "Temperature ==>", temperature, "\n",
      "Top-p Sampling ==>", top_p, "\n",
      "Presence Penalty ==>", presence_penalty, "\n",
      "---------------------------------------------------------------------------------------------------------------------------------")


prompt = "“While the current government has shown several improvements in some areas, I feel they aren’t even trying in some key areas. It pains me to see half-hearted work and empty promises that are filling the public up with false hope. On the other hand, I do understand that change takes time and not any government can work on all the changes they promise in a short tenure of 4 years. I acknowledge some hope for sure but I feel like I am moving farther away from the ray of light.” Sentiment – There is a mixture of emotions presented in this sentence. The first sentence has two parts, the first part is critical hence, negative and the second part is appreciative, hence, positive.  The second sentence depicts negative emotion. The third sentence displays hope, so positive. Fourth sentence shows negative sentiment. Since, the dominating sentiment is negative, the overall sentiment of this statement can be considered Negative. “The new software update looks great and introduces some very useful features, but it’s filled with bugs that make it nearly impossible to use efficiently. I appreciate the effort to innovate, but the lack of attention to quality control is incredibly disappointing. I really want to love it, but it's just not there yet. Although, it looks very promising to me and if it is all the good things they say it is, I am totally sold.”  Sentiment – [Your Answer]"


response = openai.ChatCompletion.create(
  api_key="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",
  model=model,
  # model="gpt-4",
  # model="gpt-4-turbo-preview",
  messages=[{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],
  temperature=temperature,  # Set the temperature
  max_tokens=1000,   # Limit the response length
  top_p=top_p,        # Apply top-p sampling
  frequency_penalty=0,  # No frequency penalty
  presence_penalty=presence_penalty  # Encourage introducing new topics
)

print("Model ==>", model, "\n",
  "Prompt ==>", prompt, "\n",
      "Response ==>", response["choices"][0]["message"]["content"], "\n",
      "Temperature ==>", temperature, "\n",
      "Top-p Sampling ==>", top_p, "\n",
      "Presence Penalty ==>", presence_penalty, "\n",
      "---------------------------------------------------------------------------------------------------------------------------------")


prompt = "“The event was very well-organized, and the guest speakers were smart and well-versed. But I felt that the venue was too small for audience, and the sound system kept malfunctioning, making it harder and harder to hear the presentations clearly. Overall, I enjoyed parts of the experience, but the technical difficulties were frustrating.” Sentiment - Branch 1: Sentiment - Positive, Node 1: The first sentence, “the event was well-organized”, shows effective planning. Node 2: The second part of the first sentence, “The speakers were smart and well-versed”, indicates that the content was valuable and informative. Branch 1 Sentiment Evaluation: The user expresses clear positive sentiments about the event’s organization and the quality of the speakers. Branch 2: Sentiment - Negative, Node 1: The second sentence, “But I felt that the venue was too small for audience”, which suggests it caused discomfort due to overcrowding. Node 2: The second part of the second sentence, “The sound system kept malfunctioning, making it harder and harder to hear the presentations clearly”, states technical frustrations. Branch 2 Sentiment Evaluation: The user highlights multiple negative aspects of the event related to the physical setting and technical issues, contributing to dissatisfaction. Branch 3: Sentiment - Neutral, Node 1: The user acknowledges that parts of the experience were enjoyable, showing a blend of positive feelings. Node 2: However, the overall tone is tempered by frustration, as technical difficulties detracted from the experience. Branch 3 Sentiment Evaluation: The user’s sentiment is mixed, reflecting an appreciation for certain elements but frustration with others. Overall Sentiment – There seems to be more of negative sentiment going on and the final concluding statement also has a hint of negativity, so the overall sentiment of the text is Negative. “I really wanted to like this new phone. It has a stunning design, and the camera quality is amazing, but the battery life is terrible, and it keeps freezing during important tasks. While I appreciate the innovation, these issues make it hard to justify the price. I'm torn because it’s almost perfect, but the flaws are just too significant to ignore.” Sentiment – [Your Answer]"


response = openai.ChatCompletion.create(
  api_key="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",
  model=model,
  # model="gpt-4",
  # model="gpt-4-turbo-preview",
  messages=[{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],
  temperature=temperature,  # Set the temperature
  max_tokens=1000,   # Limit the response length
  top_p=top_p,        # Apply top-p sampling
  frequency_penalty=0,  # No frequency penalty
  presence_penalty=presence_penalty  # Encourage introducing new topics
)

print("Model ==>", model, "\n",
  "Prompt ==>", prompt, "\n",
      "Response ==>", response["choices"][0]["message"]["content"], "\n",
      "Temperature ==>", temperature, "\n",
      "Top-p Sampling ==>", top_p, "\n",
      "Presence Penalty ==>", presence_penalty, "\n",
      "---------------------------------------------------------------------------------------------------------------------------------")

