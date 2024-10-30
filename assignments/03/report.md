your PDF report should be 2-3 pages including figures /
tables and contain the following:
• A detailed description of your experiment setup (Why did you chose these two strategies?
What data did you use? How did you preprocess it? What changes did you make in
the code? Which hyper-parameters did you use for training your models? What training
commands did you use? How did you evaluate your models? ...)

• A suitable presentation and discussion of your results compared to the baseline (table,
visualization, qualitative analysis, ...)

• A final remark on what you learned in this assignment and what you would do differently
next time

adapting hyps: 
![image](https://github.com/user-attachments/assets/06c8d925-b035-4b5e-bd7b-546fb587a5bc)
([Sennrich and Zhang, 2019, p. 4])

most promising: probably easy do modify in code: 
neuron dropout in the paper they used 0.5
reduce batch size :     parser.add_argument('--batch-size', default=1, type=int, help='maximum number of sentences in a batch')
(word) dropout in the paper they used 0.3
model depth 
