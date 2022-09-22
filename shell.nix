with import <nixpkgs> {};

/* let svg_turtle = python3.pkgs.buildPythonPackage rec {
  pname = "svg_turtle";
  version = "0.4.0";
  buildInputs = with pkgs.python39Packages; [ svgwrite ];
  src = python3.pkgs.fetchPypi {
    inherit pname version;
    sha256 = "sha256-t30apK8aTrjGUXWJL9Rg2SEmNygCD5gCYph/rTCYabY=";
  };
}; in */

let pythonPackages = with pkgs.python39Packages; [
  tqdm
  numpy
  telethon
  python-dotenv
]; in

pkgs.mkShell {
	buildInputs = with pkgs; [ python39 pythonPackages ];
}
