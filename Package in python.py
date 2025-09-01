#-------------------------------Package-------------------------------------------------
# Packages are a way of structuring Python's module namespace by using "dotted module names."
# A packages can have one or more modules which means a package is collection of modules and
# packages.
# A packages can contain packages.
# Packages is nothing but a Directory/Folder.

#                             Creating Packages
# Packages is nothing but aDirectory/Floder which MUST contain a special file called
# __init__.py.

#__init__.py file can be empty, it indicates that the directory it contains is a Python
# packages, so it can be imported the same way a module can be imported.

#                            How to use Packages-1
# Syntax:-import packageName.moduleName.
# Syntax:-import packageName.subPackageName.moduleName
# Ex:-import Admin.service
# Ex:-import Admin.Common.footer

# How to Access variables,Function,Methods,Class etc?

# Syntax:-packageName.moduleName.functionName()
# Syntax:-packagesName.subPackageName.moduleName.functionName()
# Ex:-Admin.service.admin_service()
# Ex:-Admin.Common.footer.admin_common_footer()

#                           How to use Packages-2
# Syntax:-from packageName import moduleName
# Syntax:-frompackageName.subPackageName import moduleName
# Ex:-from Admin import service
# Ex:-from Admin.Common import footer

# How to Access variables,Function,Methods,Class etc?

# Syntax:-moduleName.functionName()
# Ex:-service.admin_service()
# Ex:-footer.admin_common_footer()

#                           How to use Packages-3
# Syntax:-from packageName.moduleName import fun_name
# Syntax:-from packageName.subPackageName.moduleName import fun_name
# Ex:-from Admin.service import admin_service
# Ex:-from Admin.Common.footer import admin_common_footer

# How to Access Variable,Function,Method,class etc?

# Syntax:-functionName()
# Ex:-admin_service()
# Ex:-admin_common_footer()

#                                __all__
# If a package's __init__.py code defines a list named __all__,it is taken to be the list
# of module names that should be imported when from package import* is encountered.

# __all__=['dashboard','service','product']



