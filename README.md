# lightkube-models-pydantic

This is a fork from
[gtsystem/lightkube-models](https://github.com/gtsystem/lightkube-models) that
builds the models based on [Pydantic](https://github.com/pydantic).

Differences:
- Models are based on `pydantic.Model`.
- The classes in each model file are not in alphabetical order. They've been
  reordered so classes with dependencies in the same file are defined later
  than the classes they're dependent on. I suspect Pydantic isn't reading the
  whole file prior to parsing it, because it otherwise errors when it
  encounters a property on a model that is defined later in the same file.

**Note:** I have not tested this with [lightkube][] - I am only interested
(currently) in having kubernetes objects modeled in Pydantic, and
lightkube-models provided most of the code generation already.

## Usage

```sh
pip install lightkube-models-pydantic
```

```python
from lightkube.models.core_v1 import Pod
```

# lightkube-models

This is a python module containing definitions of kubernetes
models and resources to be used by [lightkube][].

The version of this package (first 3 parts `major.minor.micro`), match 
the kubernetes schema version used to generate the models.

You should install the module version matching your kubernetes installation or just
use compatible resources.

[lightkube]: https://lightkube.readthedocs.io/en/latest/
