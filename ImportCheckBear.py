from coalib.bearlib.abstractions.Linter import linter



class ImportCheckBear:
    """
    Find problems in C++ source code that slow down development in large code
    bases. This includes finding unused code, among other features.
    """

    LANGUAGES = {'CPP'}
    REQUIREMENTS = {PipRequirement('cppclean', '0.12.0')}
    AUTHORS = {'Elymas Zhakata'}
    AUTHORS_EMAILS = {'ezhakata@gmail.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Incorrect diclaration'}

    def create_arguments(filename,
                         file,
                         config_file,
                         include_paths: typed_list(str) = (),
                         ):
        args = [filename]
        for include_path in include_paths:
            args.append('--include-path')
            args.append(include_path)

        return args
