from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.files import update_conandata
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class pkg1Recipe(ConanFile):
	name = "pkg1"
	version = "1.0"

	# Optional metadata
	license = "<Put the package license here>"
	author = "<Put your name here> <And your email here>"
	url = "<Package recipe repository url here, for issues about the package>"
	description = "<Description of pkg1 package here>"
	topics = ("<Put some tag here>", "<here>", "<and here>")

	# Binary configuration
	settings = "os", "compiler", "build_type", "arch"
	options = {"shared": [True, False], "fPIC": [True, False]}
	default_options = {"shared": False, "fPIC": True}

	def layout(self):
		self.folders.root = ".."
		self.folders.subproject = "pkg1"
		cmake_layout(self)
	
	def export(self):
		git = Git(self, self.recipe_folder)
		scm_url, scm_commit = git.get_url_and_commit()
		update_conandata(self, {"sources": {"commit": scm_commit, "url": scm_url}})

	def source(self):
		git = Git(self)
		sources = self.conan_data["sources"]
		git.clone(url=sources["url"], target=".")
		git.checkout(commit=sources["commit"])

	def generate(self):
		deps = CMakeDeps(self)
		deps.generate()
		tc = CMakeToolchain(self)
		tc.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()

	def package_info(self):
		self.cpp_info.libs = ["pkg1"]
