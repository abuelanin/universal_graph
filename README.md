---


---

<h1 id="universal-genome-graph-project">Universal Genome Graph Project</h1>
<p>The aim of the project is to identify genes that extracted from weak genomes.</p>
<h1 id="features">Features!</h1>
<ul>
<li>Convert FASTA files to Graphical Fragment Assembly format (GFA 1).</li>
<li>Extract the No. of the disconnected graphs with different k-mer values.</li>
</ul>
<h3 id="used-programs">Used programs:</h3>

<table>
<thead>
<tr>
<th>Program</th>
<th>README</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bcalm2</td>
<td><a href="https://github.com/GATB/bcalm/blob/master/README.md">https://github.com/GATB/bcalm/blob/master/README.md</a></td>
</tr>
<tr>
<td>Bandage</td>
<td><a href="https://github.com/rrwick/Bandage/blob/master/README.md">https://github.com/rrwick/Bandage/blob/master/README.md</a></td>
</tr>
</tbody>
</table><blockquote>
<p>We’ve used Bcalm to generate the unitigs for the sequence then convert the unitigs to GFA.
Bandage is used to extract the connected graphs number.</p>
</blockquote>
<h3 id="installation-linux-tested-on-ubuntu">Installation (Linux) Tested on Ubuntu</h3>
<h5 id="clone-the-universal-graph-repository">Clone the Universal Graph repository</h5>
<pre class=" language-sh"><code class="prism  language-sh">git clone https://github.com/abuelanin/universal_graph.git
</code></pre>
<h5 id="install-the-dependencies">Install the dependencies</h5>
<p>– GCC &gt;= 4.8 or a very recent C++11 capable compiler</p>
<pre class=" language-sh"><code class="prism  language-sh">sudo apt-get update
apt-get install build-essential
sudo apt-get install g++ gcc
sudo apt-get update
</code></pre>
<p>– QT5
Install the dependencies and devDependencies and start the server.</p>
<pre class=" language-sh"><code class="prism  language-sh">sudo apt-get update
sudo apt-get install build-essential git qtbase5-dev libqt5svg5-dev
export QT_SELECT=5
</code></pre>
<p>Download and install Bcalm</p>
<pre class=" language-sh"><code class="prism  language-sh">git clone --recursive https://github.com/GATB/bcalm 
cd bcalm
mkdir build;  cd build;  cmake ..;  make -j 8
cd ../../
</code></pre>
<p>Download and install Bandage</p>
<pre class=" language-sh"><code class="prism  language-sh">sudo apt-get update
git clone https://github.com/rrwick/Bandage.git
cd Bandage
qmake
make
cd ..
</code></pre>
<blockquote>
<p>Optionally, copy the program into /usr/local/bin:<code>sudo make install</code>. The Bandage build directory can then be deleted.</p>
</blockquote>

