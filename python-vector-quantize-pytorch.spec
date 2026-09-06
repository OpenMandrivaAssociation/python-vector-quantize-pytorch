Name:		python-vector-quantize-pytorch
Version:	1.27.15
Release:	3
Summary:	Vector quantization layers for PyTorch
License:	MIT
Group:		Development/Python
URL:		https://github.com/lucidrains/vector-quantize-pytorch
Source0:	https://files.pythonhosted.org/packages/source/v/vector-quantize-pytorch/vector_quantize_pytorch-%{version}.tar.gz
Patch0:		0001-optional-torch-distributed-nn.patch
Patch1:		0002-residual-fsq-meta-device-assert.patch
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
Requires:	python%{pyver}dist(einops)
Requires:	python%{pyver}dist(einx)
Requires:	python%{pyver}dist(torch)

%description
Vector (and residual FSQ) quantization modules for PyTorch.
ACE-Step 1.5 uses ResidualFSQ in its DiT tokenizer.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/vector_quantize_pytorch
%{py_sitedir}/vector_quantize_pytorch-*.*-info
