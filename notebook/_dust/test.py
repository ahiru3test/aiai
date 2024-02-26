try:
    from sklearnex import patch_sklearn, unpatch_sklearn
    patch_sklearn()
except ModuleNotFoundError:
    print("Extension for Scikit-learn* is not enabled")
    pass
