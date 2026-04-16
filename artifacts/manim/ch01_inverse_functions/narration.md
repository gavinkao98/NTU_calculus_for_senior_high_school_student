# ch01_inverse_functions Final Narration

Source file: `inputs\manim_storyboards\ch01_inverse_functions.yml`
Deck ID: `ch01_inverse_functions`

You may edit the narration text below each **Narration:** heading.
Do NOT change the Slide ID lines — they are used to match edits back to the correct scene.
After editing, run `python tools/sync_narration_back.py --deck-id ch01_inverse_functions` to write changes back to the storyboard YAML.

## Slide 1: Inverse Functions

Slide ID: `opening_hook`
Scene template: `title_bullets`

Narration:

Every function is a machine: you feed in a number, it hands you back another. But sometimes we want to run the machine backwards. If a formula converts Celsius into Fahrenheit, there should be another formula that converts Fahrenheit back into Celsius. The question is: when can we actually reverse a function, and when is it impossible? That is the subject of this video.

## Slide 2: One-to-One Functions

Slide ID: `one_to_one_definition`
Scene template: `definition_math`

Narration:

The key property is called one-to-one. A function is one-to-one when different inputs always produce different outputs. No two distinct x-values ever land on the same y-value. There is an equivalent way to say this: if you know that f of x one equals f of x two, then you can conclude that x one must equal x two. Both statements capture the same idea, but the second form is often easier to use in a proof.

## Slide 3: A Concrete Example

Slide ID: `real_world_one_to_one`
Scene template: `example_walkthrough`

Narration:

Before we look at algebraic functions, consider a simple real-world test. Assign each student in a class their student ID number. Every student gets a unique ID, so if two students are different people, they must have different IDs. That function is one-to-one. Now assign each student their blood type. Alice and Bob can both be Type O. Two different inputs share the same output. That function is not one-to-one. The lesson: ask whether a single output can be traced back to two different inputs.

## Slide 4: Testing with Algebra

Slide ID: `algebraic_one_to_one_test`
Scene template: `example_walkthrough`

Narration:

Now let us test two mathematical functions. Take f of x equals x on the interval zero to one. If x one is different from x two, then f of x one equals x one is certainly different from f of x two equals x two. So this function is one-to-one. Now consider g of x equals x squared on minus one to one. Here, one half and negative one half are different inputs, but they both square to one fourth. Two inputs, same output. So g is not one-to-one on this interval.

## Slide 5: Why x-squared Cannot Be Inverted

Slide ID: `why_x_squared_fails`
Scene template: `graph_focus`

Narration:

Let us see this failure on a graph. Here is the parabola y equals x squared on minus one to one. The output one fourth sits at this height. A horizontal line at that level crosses the curve in two places: at x equals one half on the right and x equals minus one half on the left. If we tried to define g inverse of one fourth, we would have to choose between two inputs. A function cannot return two answers. So g inverse of one fourth is simply not well defined.

## Slide 6: The Horizontal Line Test

Slide ID: `horizontal_line_test`
Scene template: `definition_math`

Narration:

There is a quick visual rule that captures this idea. Draw any horizontal line y equals c across the graph. That line represents a fixed output value. If it crosses the graph more than once, then two different x-values are producing the same output, so the function is not one-to-one. If every horizontal line hits the graph at most once, then every output comes from a unique input, and the function is one-to-one. This is called the horizontal line test.

## Slide 7: Horizontal Line Test in Action

Slide ID: `horizontal_line_test_figure`
Scene template: `graph_focus`

Narration:

On the left is a straight line: every horizontal level crosses it exactly once. That graph passes the horizontal line test. On the right is a parabola. A horizontal line at the right height crosses it twice, once on each side of the axis of symmetry. That graph fails the test. Whenever you see a graph, this sweep is the fastest way to check whether an inverse can exist.

## Slide 8: Defining the Inverse

Slide ID: `transition_to_inverses`
Scene template: `section_transition`

Narration:

Now that we know what one-to-one means, we can define the inverse function itself.

## Slide 9: The Inverse Function

Slide ID: `inverse_definition`
Scene template: `definition_math`

Narration:

Here is the definition. Suppose f is one-to-one with domain A and range B. Its inverse, written f inverse, has domain B and range A, and it is defined by the rule: f inverse of y equals x if and only if f of x equals y. In other words, the inverse simply reverses the direction of the original function. The outputs of f become the inputs of f inverse, and the inputs of f become the outputs of f inverse.

## Slide 10: When Does an Inverse Exist?

Slide ID: `existence_theorem`
Scene template: `theorem_proof`

Narration:

The central theorem is clean: a function has an inverse if and only if it is one-to-one. The forward direction is straightforward. If f has an inverse, and f of x one equals f of x two, then applying f inverse to both sides gives x one equals x two. So f must be one-to-one. For the converse, if f is one-to-one, then for each output y in the range, there is exactly one x that maps to it. That unique correspondence defines f inverse.

## Slide 11: The Cancellation Equations

Slide ID: `composition_identities`
Scene template: `definition_math`

Narration:

The inverse literally undoes the original function. This gives us two composition identities that are worth memorizing. First: f inverse of f of x equals x for every x in the domain of f. You apply f, then undo it with f inverse, and you land back where you started. Second: f of f inverse of x equals x for every x in the range of f. You apply f inverse, then apply f, and again you return to the starting point. These two identities also serve as a verification tool: if you find a candidate for f inverse, check that both compositions give x.

## Slide 12: How to Find an Inverse

Slide ID: `finding_inverse_procedure`
Scene template: `procedure_steps`

Narration:

When you know a function is one-to-one, finding its inverse is a mechanical procedure. Step one: write y equals f of x. Step two: solve that equation for x in terms of y. This is usually the hardest step, because it depends on the algebra of f. Step three: interchange x and y. That last swap is not just cosmetic. It rewrites the inverse as a function of x, which is the standard convention.

## Slide 13: Worked Example: f(x) = x cubed + 2

Slide ID: `example_cubic`
Scene template: `example_walkthrough`

Narration:

Let us apply the procedure to f of x equals x cubed plus two. Step one: write y equals x cubed plus two. Step two: subtract two, giving x cubed equals y minus two. Then take the cube root: x equals the cube root of y minus two. Step three: interchange x and y. So f inverse of x equals the cube root of x minus two. Finally, let us verify. Compute f of f inverse of x: plug the cube root of x minus two into x cubed plus two. The cube and the cube root cancel, giving x minus two plus two, which is x. The cancellation equation checks out.

## Slide 14: Graphs of f and f-inverse

Slide ID: `cubic_graph_reflection`
Scene template: `graph_focus`

Narration:

Here is a beautiful geometric fact. The graph of f of x equals x cubed plus two is this S-shaped curve shifted up by two. The graph of its inverse, the cube root of x minus two, is the mirror image reflected across the line y equals x. Every point a, b on the graph of f corresponds to the point b, a on the graph of f inverse. The dashed line y equals x is the mirror. This reflection property holds for every invertible function and its inverse.

## Slide 15: Restricting the Domain of x-squared

Slide ID: `domain_restriction_idea`
Scene template: `example_walkthrough`

Narration:

Earlier we saw that x squared on minus one to one is not one-to-one. But what if we restrict the domain? On the interval x greater than or equal to zero, the parabola is strictly increasing: larger inputs always give larger outputs. So x squared on this restricted domain is one-to-one. We can now find its inverse. Write y equals x squared with x at least zero. Solve: x equals the square root of y, choosing the nonnegative root because the original domain requires x at least zero. Interchange x and y: f inverse of x equals the square root of x.

## Slide 16: x-squared and square-root as Reflections

Slide ID: `restricted_parabola_graph`
Scene template: `graph_focus`

Narration:

On the restricted domain, the graph of x squared is the right half of the parabola. Its inverse, the square root function, is the reflection across y equals x. Notice how the two curves are symmetric about the dashed diagonal. This is the same reflection principle we saw with the cubic, and it works for any invertible function. The key insight is that domain restriction turned a non-invertible function into an invertible one.

## Slide 17: Key Takeaways

Slide ID: `recap`
Scene template: `recap_cards`

Narration:

Let us summarize what we have learned. A function is one-to-one when no two inputs share the same output. The horizontal line test is a quick visual check for this property. A function has an inverse if and only if it is one-to-one. To find the inverse, write y equals f of x, solve for x, then swap x and y. The cancellation equations let you verify your answer. And the graph of f inverse is the reflection of f across the line y equals x. If a function is not one-to-one on its full domain, restricting the domain can make it invertible.
