import os.path
import torchvision.transforms as transforms
from data.base_dataset import BaseDataset, get_transform
from data.image_folder import make_dataset
from PIL import Image


class DoubleDataset(BaseDataset):
    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot
        self.dir_A = os.path.join(opt.dataroot, 'A')
        self.dir_B = os.path.join(opt.dataroot, 'B')

        self.A_paths = make_dataset(self.dir_A)

        self.A_paths = sorted(self.A_paths)

        self.B_paths = make_dataset(self.dir_B)

        self.B_paths = sorted(self.B_paths)

        self.transform = get_transform(opt)

    def __getitem__(self, index):
        A_path = self.A_paths[index]

        A_img = Image.open(A_path).convert('RGB')

        A_img = self.transform(A_img)

        B_path = self.B_paths[index]

        B_img = Image.open(B_path).convert('RGB')

        B_img = self.transform(B_img)

        print('A_path: ' + A_path)
        print('B_path: ' + B_path)

        return {'A': A_img, 'A_paths': A_path, 'B': B_img, 'B_paths': B_path}

    def __len__(self):
        return len(self.A_paths)

    def name(self):
        return 'SingleImageDataset'
