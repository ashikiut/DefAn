# DefAn: Definitive-Answer-Dataset-for-LLMs-Hallucination-Evaluation

<div align="center">
  A.B.M. Ashikur Rahman<sup>1</sup>, Saeed Anwar<sup>1,2</sup>, Muhammad Usman<sup>1,2</sup>, Ajmal Mian<sup>3</sup>, 
</div>
<div align="center">
<sup>1</sup> King Fahd University of Petroleum and Minerals 
</div>
<div align="center">
<sup>2</sup>JRCAI, SDAIA-KFUPM 
</div>
<div align="center">
<sup>3</sup>The University of Western Australia
</div>
<div align="center">
    <a href="https://arxiv.org/abs/2406.09155">Arxiv Paper</a>,  <a href="https://huggingface.co/datasets/iamasQ/DefAn">Hugging Face Repository</a>
</div>

### Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities, revolutionizing the integration of AI in daily life applications. However, they are prone to hallucinations, generating claims that contradict established facts, deviating from prompts, and producing inconsistent responses when the same prompt is presented multiple times. Addressing these issues is challenging due to the lack of comprehensive and easily assessable benchmark datasets. Most existing datasets are small and rely on multiple-choice questions, which are inadequate for evaluating the generative prowess of LLMs. To measure hallucination in LLMs, this paper introduces a comprehensive benchmark dataset comprising over 75,000 prompts across eight domains. These prompts are designed to elicit definitive, concise, and informative answers. The dataset is divided into two segments: one publicly available for testing and assessing LLM performance and a hidden segment for benchmarking various LLMs. In our experiments, we tested six LLMs—GPT-3.5, LLama 2, LLama 3, Gemini, Mixtral, and Zephyr—revealing that overall factual hallucination ranges from 59\% to 82\% on the public dataset and 57\% to 76\% in the hidden benchmark. Prompt misalignment hallucination ranges from 6\% to 95\% in the public dataset and 17\% to 94\% in the hidden counterpart. Average consistency ranges from 21\% to 61\% and 22\% to 63\%, respectively. Domain-wise analysis shows that LLM performance significantly deteriorates when asked for specific numeric information while performing moderately with person, location, and date queries. Our dataset demonstrates its efficacy and serves as a comprehensive benchmark for LLM performance evaluation.

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

### LLM Evaluation
In this paper we evalated 6 widely used LLMs on the metrics proposed. These models are- gpt 3.5, Llama-2, Llama-3, zephyr, gemini 1.0 pro, mixtral.
Domain wise performance for each LLM is summarized here.
#### FCH Rate:
|         | Sports |        | Census |        |  Nobel |        | Entertainment |        | World Organizations |        | QS Ranking |        | Conf. Venue |        |  Math  |        |
|---------|:------:|:------:|:------:|:------:|:------:|:------:|:-------------:|:------:|:-------------------:|:------:|:----------:|:------:|:-----------:|:------:|:------:|:------:|
|         | Public | Hidden | Public | Hidden | Public | Hidden |     Public    | Hidden |        Public       | Hidden |   Public   | Hidden |    Public   | Hidden | Public | Hidden |
| zephyr  |  0.50  |  0.29  |  1.00  |  1.00  |  0.91  |  0.93  |      0.68     |  0.20  |         0.95        |  0.92  |    0.94    |  0.98  |     0.82    |  0.95  |  0.99  |  0.99  |
| mixtral |  0.20  |  0.13  |  1.00  |  1.00  |  0.59  |  0.60  |      0.56     |  0.11  |         0.69        |  0.44  |    0.88    |  0.98  |     0.52    |  0.63  |  0.98  |  0.97  |
| llama3  |  0.44  |  0.30  |  1.00  |  1.00  |  0.63  |  0.70  |      0.29     |  0.19  |         0.71        |  0.73  |    0.97    |  0.99  |     0.65    |  0.87  |  1.00  |  0.99  |
| llama2  |  0.15  |  0.09  |  1.00  |  1.00  |  0.90  |  0.90  |      0.33     |  0.17  |         0.85        |  0.74  |    0.93    |  0.99  |     0.85    |  0.88  |  0.98  |  0.98  |
| gpt 3.5 |  0.17  |  0.11  |  1.00  |  1.00  |  0.35  |  0.52  |      0.10     |  0.19  |         0.57        |  0.38  |    0.93    |  0.98  |     0.31    |  0.60  |  0.98  |  0.98  |
| gemini  |  0.21  |  0.09  |  1.00  |  1.00  |  0.35  |  0.52  |      0.42     |  0.14  |         0.54        |  0.31  |    0.97    |  0.96  |     0.47    |  0.51  |  0.99  |  0.99  |

#### PMH Rate:
|         | Sports |        | Census |        |  Nobel |        | Entertainment |        | World Organizations |        | QS Ranking |        | Conf. Venue |        |  Math  |        |
|---------|:------:|:------:|:------:|:------:|:------:|:------:|:-------------:|:------:|:-------------------:|:------:|:----------:|:------:|:-----------:|:------:|:------:|:------:|
|         | Public | Hidden | Public | Hidden | Public | Hidden |     Public    | Hidden |        Public       | Hidden |   Public   | Hidden |    Public   | Hidden | Public | Hidden |
| zephyr  |  0.87  |  0.98  |  1.00  |  1.00  |  0.96  |  0.98  |      0.76     |  0.41  |         0.99        |  0.99  |    1.00    |  1.00  |     1.00    |  1.00  |  1.00  |  1.00  |
| mixtral |  0.95  |  0.89  |  1.00  |  1.00  |  0.94  |  0.99  |      0.87     |  0.71  |         1.00        |  1.00  |    1.00    |  1.00  |     0.97    |  0.99  |  0.98  |  0.98  |
| llama3  |  0.18  |  0.34  |  0.98  |  0.99  |  0.16  |  0.26  |      0.01     |  0.03  |         0.78        |  0.74  |    0.52    |  0.56  |     0.24    |  0.26  |  0.04  |  0.04  |
| llama2  |  0.07  |  0.09  |  0.96  |  0.99  |  0.48  |  0.85  |      0.04     |  0.01  |         0.74        |  0.72  |    1.00    |  0.99  |     0.64    |  0.57  |  0.02  |  0.01  |
| gpt 3.5 |  0.17  |  0.16  |  0.55  |  0.49  |  0.14  |  0.41  |      0.31     |  0.33  |         0.75        |  0.88  |    0.55    |  0.62  |     0.17    |  0.22  |  0.38  |  0.36  |
| gemini  |  0.06  |  0.05  |  0.01  |  0.00  |  0.12  |  0.36  |      0.06     |  0.01  |         0.57        |  0.80  |    0.04    |  0.00  |     0.27    |  0.20  |  0.01  |  0.02  |

#### Response Consistency
|         | Sports |        | Census |        |  Nobel |        | Entertainment |        | World Organizations |        | QS Ranking |        | Conf. Venue |        |
|---------|:------:|:------:|:------:|:------:|:------:|:------:|:-------------:|:------:|:-------------------:|:------:|:----------:|:------:|:-----------:|:------:|
|         | Public | Hidden | Public | Hidden | Public | Hidden |     Public    | Hidden |        Public       | Hidden |   Public   | Hidden |    Public   | Hidden |
| zephyr  |  0.19  |  0.15  |  0.07  |  0.07  |  0.10  |  0.11  |      0.43     |  0.59  |         0.13        |  0.15  |    0.13    |  0.10  |     0.47    |  0.43  |
| mixtral |  0.19  |  0.28  |  0.07  |  0.07  |  0.12  |  0.09  |      0.38     |  0.26  |         0.13        |  0.22  |    0.07    |  0.07  |     0.78    |  0.74  |
| llama3  |  0.60  |  0.62  |  0.07  |  0.07  |  0.46  |  0.52  |      0.81     |  0.84  |         0.50        |  0.46  |    0.11    |  0.08  |     0.58    |  0.50  |
| llama2  |  0.94  |  0.97  |  0.07  |  0.07  |  0.36  |  0.21  |      0.96     |  0.97  |         0.28        |  0.31  |    0.09    |  0.07  |     0.47    |  0.43  |
| gpt 3.5 |  0.77  |  0.86  |  0.07  |  0.07  |  0.80  |  0.62  |      0.67     |  0.66  |         0.28        |  0.23  |    0.21    |  0.15  |     0.84    |  0.73  |
| gemini  |  0.82  |  0.91  |  0.07  |  0.07  |  0.79  |  0.74  |      0.89     |  0.99  |         0.79        |  0.82  |    0.15    |  0.16  |     0.78    |  0.76  |

#### Overall Performance

### Citation Information

```bibtex
@article{rahman2024defan,
  title={DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation},
  author={Rahman, ABM and Anwar, Saeed and Usman, Muhammad and Mian, Ajmal},
  journal={arXiv preprint arXiv:2406.09155},
  year={2024}
}

```
