/*
 * sst-plugininfra - an open source library of plugin infrastructure
 * built by Surge Synth Team.
 *
 * Copyright 2018-2024, various authors, as described in the GitHub
 * transaction log.
 *
 * sst-effects is released under the MIT License. It has subordinate
 * libraries with licenses as described in libs/
 *
 * All source in sst-plugininfra available at
 * https://github.com/surge-synthesizer/sst-plugininfra
 */

#include <sst/plugininfra/version_information.h>

static_assert("55ea1fe"[0] != '\0',
              "GIT_COMMIT_HASH not defined. Run cmake/git-version-functions.cmake commands to use "
              "this library");
namespace sst::plugininfra
{
// clang-format off
const char *VersionInformation::git_commit_hash{"55ea1fe"};
const char *VersionInformation::git_branch{"HEAD"};
const char *VersionInformation::git_tag{"v1.0.5"};
const char *VersionInformation::git_implied_display_version{"v1.0.5"};

const char *VersionInformation::project_version_major{"1"};
const char *VersionInformation::project_version_minor{"0"};
const char *VersionInformation::project_version_patch{"5"};
const char *VersionInformation::project_version_tweak{"0"};
const char *VersionInformation::project_version{
    "1.0.5"};
const char *VersionInformation::project_version_and_hash{
    "1.0.5.55ea1fe"};

const char *VersionInformation::project_version_full{
    "1.0.5.0"};

const char *VersionInformation::cmake_source_dir{"/tmp/six-sines"};
const char *VersionInformation::cmake_binary_dir{"/tmp/six-sines/build"};
const char *VersionInformation::cmake_install_prefix{"/usr/local"};
const char *VersionInformation::cmake_compiler_id{"GNU"};
const char *VersionInformation::cmake_compiler_version{"14.2.1"};
const char *VersionInformation::cmake_compiler{
    "GNU-14.2.1"};
const char *VersionInformation::cmake_system_name{"Linux"};

const char *VersionInformation::build_date{"2025-01-20"};
const char *VersionInformation::build_year{"2025"};
const char *VersionInformation::build_time{"20:15:43"};
// clang-format on
} // namespace sst::plugininfra
