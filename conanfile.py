from conans import ConanFile, CMake, tools


class LowioConan(ConanFile):
    name = "LowIO"
    version = "1.0"
    license = "MIT"
    url = "https://github.com/objectx/lowio"
    description = "Cross platform handle based I/O"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/objectx/lowio.git")
        self.run("cd lowio && git checkout develop")

    def build(self):
        self.run('conan install %s/lowio' % (self.source_folder))
        cmake = CMake(self)
        cmake.configure(source_folder="lowio")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.hpp", dst="include", src="lowio/include")
        self.copy("*lowio.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lowio"]
