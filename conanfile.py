from conans import ConanFile, CMake, tools


class GhostmoduleConan(ConanFile):
    name = "ghostmodule"
    version = "1.2"
    license = "Apache License 2.0"
    author = "Mathieu Nassar mathieu.nassar@gmail.com"
    url = "https://github.com/mathieunassar/ghostmodule"
    description = "Lightweight, multiplatform and accessible framework for command line-based programs and C++ microservices."
    topics = ("framework", "microservice", "command-line")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    requires = (
        "protobuf/3.6.1@bincrafters/stable",
        "protoc_installer/3.6.1@bincrafters/stable"
    )

    def source(self):
        git = tools.Git(folder="ghostmodule")
        git.clone("https://github.com/mathieunassar/ghostmodule.git", "v1.2")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="ghostmodule", args=["-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE"])
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy('*', dst='include', src='ghostmodule/include')
        self.copy("*.lib", dst="lib", src="", keep_path=False)
        self.copy("*.a", dst="lib", src="", keep_path=False)
        self.copy("*", dst="bin", src="bin")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["ghost_moduled", "ghost_persistenced"]
        else:
            self.cpp_info.libs = ["ghost_module", "ghost_persistence"]
