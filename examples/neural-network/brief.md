# Scientific and visual brief

Assumption: artificial neural network, rather than a biological neural circuit. Original conceptual 4–5–5–3 fully connected classifier with two ReLU hidden layers and one coupled softmax output. No measured data, trained weights or model performance implied.

- Show exactly 17 activation/logit nodes and 60 adjacent-layer weighted connections. Column-vector convention: W1 is 5×4, W2 is 5×5 and W3 is 3×5. Bias vectors have 5, 5 and 3 elements respectively.
- Forward computation is left to right. Hidden activation h = ReLU(Wa+b). Output logits undergo one vector-valued softmax, not three independent sigmoids.
- Single-unit inset includes weights, bias, affine sum and ReLU. The ReLU curve is derived from max(0,z), not observations.
- Training is a separate symbolic strip: prediction and one-hot target enter cross-entropy; backpropagation computes gradients; gradient descent updates parameters. No feedback edge is part of inference.
- Refined editorial design: white background, muted layer-specific colours, round nodes with restrained gradients, thin connections, bold panel labels and uncluttered mathematical annotation. Solid forward flow and dashed amber training-gradient flow have explicit labels.
- Deliver PNG exported from full-vector SVG, image2 visual master, generator, editable labels/nodes/edges and saved editor test. Intended wide overview, not a claim of narrow journal-column compliance.
