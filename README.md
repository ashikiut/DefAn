# DefAn: Definitive-Answer-Dataset-for-LLMs-Hallucination-Evaluation

### Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities, revolutionizing the integration of AI in daily life applications. However, they are prone to hallucinations, generating claims that contradict established facts, deviating from prompts, and producing inconsistent responses when the same prompt is presented multiple times. Addressing these issues is challenging due to the lack of comprehensive and easily assessable benchmark datasets. Most existing datasets are small and rely on multiple-choice questions, which are inadequate for evaluating the generative prowess of LLMs. To measure hallucination in LLMs, this paper introduces a comprehensive benchmark dataset comprising over 75,000 prompts across eight domains. These prompts are designed to elicit definitive, concise, and informative answers. The dataset is divided into two segments: one publicly available for testing and assessing LLM performance and a hidden segment for benchmarking various LLMs. In our experiments, we tested six LLMs—GPT-3.5, LLama 2, LLama 3, Gemini, Mixtral, and Zephyr—revealing that overall factual hallucination ranges from 59\% to 82\% on the public dataset and 57\% to 76\% in the hidden benchmark. Prompt misalignment hallucination ranges from 6\% to 95\% in the public dataset and 17\% to 94\% in the hidden counterpart. Average consistency ranges from 21\% to 61\% and 22\% to 63\%, respectively. Domain-wise analysis shows that LLM performance significantly deteriorates when asked for specific numeric information while performing moderately with person, location, and date queries. Our dataset demonstrates its efficacy and serves as a comprehensive benchmark for LLM performance evaluation.


<!-- Provide a quick summary of the dataset. -->
[[Paper]](https://arxiv.org/abs/2406.09155) [[Github Repo]](https://github.com/ashikiut/DefAn)

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
**Purpose:** Evaluation benchmark for LLM hallucinations.<br>

**Structure:** Two-part dataset:<br>
- Public: Available for general evaluation.<br>
- Hidden: Used for benchmarking, ensuring comprehensive assessment.<br>

**Evaluation Metrices:**
- Fact Contradicting Hallucination (FCH) rate
- Prompt Misalignment Hallucination (PMH) rate
- Response Consistency (RC)

**Size:** Over 75,000 samples, providing a substantial volume of data for rigorous testing.<br>

### Domain Statistics
|                     | **\# of samples** |            | *Response type* |             |             |             |                 |
| :------------------ | :---------------: | :--------: | :-------------- | :---------- | :---------- | :---------- | :-------------: |
| **Domains**         | **Public**        | **Hidden** | *Date*          | *Numeric*   | *Name*      | *Location*  | **Paraphrased** |
| Sports              | 1305              | 1005       |        ✅      |     ✅     |     ✅     |     ✅     |      ✅     |
| Census Australia    | 7905              | 1005       |                 |     ✅     |             |             |      ✅      |
| Nobel Prize         | 9795              | 1005       |                 |             |     ✅     |             |     ✅        |
| Entertainment       | 8715              | 1005       |        ✅      |             |     ✅     |             |      ✅        |
| World Organizations | 2745              | 1005       |        ✅      |             |             |             |      ✅         |
| QS Ranking          | 21495             | 1005       |                 |     ✅     |             |             |     ✅        |
| Conference Venue    | 915               | 450        |                 |             |             |      ✅      |      ✅        |
| Math                | 15218             | 1005       |                 |     ✅     |             |             |                 |

### Data Instances
An example looks as follows:

```python
{
    "questions":"Who achieved the Nobel Prize in Medicine for the year 1901? [first name + last name only] if multiple person, give one name only.",
    "answer":"Emil von Behring",
    "type":"name"
}

```

### Languages

All the samples in this dataset is in English.

### Citation Information

```bibtex
@article{rahman2024defan,
  title={DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation},
  author={Rahman, ABM and Anwar, Saeed and Usman, Muhammad and Mian, Ajmal},
  journal={arXiv preprint arXiv:2406.09155},
  year={2024}
}

```
