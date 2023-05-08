# Wikipedia Editor Analysis

How much does Wikipedia editors stray from their domain/topic expertise?

Let each articles be represented with an ordered list of embeddings $$(a_1, a_2,..., a_m)$$
and two articles' semantic difference measured by their L2 norm $$dist(x,y) = \\sqrt{\\sum_{i=1}^m (x_i - y_i)^2}$$
 
Let each editor be represented with a list of articles that they edit and how many times they edit them $$((a_1, c_1), (a_2, c_2),..., (a_n, c_n))$$
Then, each editor's variance is $$var(x) = \\sqrt{\\frac{\\sum_{i=1}^n dist(a_i, E[x]) * c_i}{\\sum_{i=1}^n c_i}}$$
